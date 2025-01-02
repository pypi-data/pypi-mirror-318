#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 01:50:28 2024

@author: midhunmachari@gmail.com
"""

# Import libraries
import os
import time
import datetime
import warnings
import numpy as np
import pandas as pd
import xarray as xr
import tensorflow as tf
import matplotlib.pyplot as plt
from tqdm import tqdm
from tabulate import tabulate

from ..utils import make_predictions, build_netcdf_from_array, compute_metrics, CustomCSVLogger
from ..utils import negtozero, r_logtrans, plot_traincurve, build_tf_data_pipeline
from ..losses import weighted_mae, weighted_mse
from .supervised import ModelTraining

# --------------------------------------------------
# The Pix2Pix class for GAN Training and Validation
# --------------------------------------------------
class Pix2Pix(ModelTraining):
    
    def __init__(
            self, 
            prefix: str='tst',  
            save_path: str='.',
            generator=None, 
            discriminator=None, 
            gen_lr_init=2e-4,
            dis_lr_init=2e-4,
            l1_opt='WMAE',
            lambda_value=100,
            log_tensorboard = False,
            enable_function=True,
            suffix=None,
            ):
        # Initialize the parent class (ModelTraining)
        super().__init__(prefix, save_path, log_tensorboard=log_tensorboard, enable_function=enable_function, suffix=suffix)
        
        # Set specific parameters for Pix2Pix
        self.generator = generator
        self.discriminator = discriminator
        self.l1_opt = l1_opt
        self.lambda_value = lambda_value

        # Define the loss object and optimizers for Pix2Pix
        self.bce_loss = tf.keras.losses.BinaryCrossentropy(from_logits=True)
        self.generator_optimizer = tf.keras.optimizers.Adam(gen_lr_init, beta_1=0.5)
        self.discriminator_optimizer = tf.keras.optimizers.Adam(dis_lr_init, beta_1=0.5)

        if generator and discriminator:
            print(
                f"\nSRGAN training initialized with:\n"
                f"  - Generator: {self.generator.name}\n"
                f"  - Discriminator: {self.discriminator.name}\n"
                f"  - Learning Rates:\n"
                f"      Generator: {gen_lr_init}\n"
                f"      Discriminator: {dis_lr_init}"
            )

    def __str__(self):
       return (f"Pix2Pix Configuration:\n"
               f"  Exp.Name: {self.expname}\n"
               f"  Output Save Directory: {self.save_path}\n"
               f"  L1 Loss Option: {self.l1_opt}\n"
               f"  Generator Optimizer: {self.generator_optimizer.__class__.__name__} "
               f"(learning_rate={self.generator_optimizer.learning_rate.numpy()}, beta_1={self.generator_optimizer.beta_1.numpy()})\n"
               f"  Discriminator Optimizer: {self.discriminator_optimizer.__class__.__name__} "
               f"(learning_rate={self.discriminator_optimizer.learning_rate.numpy()}, beta_1={self.discriminator_optimizer.beta_1.numpy()})\n"
               f"  Lambda Value: {self.lambda_value}\n"
               f"  Enable @tf.function: {self.enable_function}\n"
               f"  Generator Model: {self.generator.name}\n"
               f"  Discriminator Model: {self.discriminator.name}")
        
    def discriminator_loss(self, disc_real_output, disc_generated_output):
        real_loss = self.bce_loss(tf.ones_like(disc_real_output), disc_real_output)
        generated_loss = self.bce_loss(tf.zeros_like(disc_generated_output), disc_generated_output)
        total_dis_loss = real_loss + generated_loss
        return total_dis_loss

    def generator_loss(self, disc_generated_output, gen_output, target):
        gan_loss = self.bce_loss(tf.ones_like(disc_generated_output), disc_generated_output)
        if self.l1_opt == 'WMAE': # Weighted Mean Absolute Error
            l1_loss = weighted_mae(target, gen_output) 
        elif self.l1_opt == 'MAE': # Mean Absolute Error
            l1_loss = self.mae_calc(target, gen_output)
        if self.l1_opt == 'WMSE': # Weighted Mean Squared Error
            l1_loss = weighted_mse(target, gen_output) 
        elif self.l1_opt == 'MSE': # Mean Squared Error
            l1_loss = self.mse_calc(target, gen_output)
        else:
            raise ValueError(f"Invalid l1_opt value: {self.l1_opt}. Expected one of 'WMAE', 'MAE', 'WMSE', 'MSE'.")
        total_gen_loss = gan_loss + (self.lambda_value * l1_loss)
        return total_gen_loss

    def train_step(self, input_image, target_image):
        with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
            gen_output = self.generator(input_image, training=True)
            disc_real_output = self.discriminator([input_image, target_image], training=True)
            disc_generated_output = self.discriminator([input_image, gen_output], training=True)
            gen_loss = self.generator_loss(disc_generated_output, gen_output, target_image)
            dis_loss = self.discriminator_loss(disc_real_output, disc_generated_output)
            mae_loss = self.mae_calc(target_image, gen_output)
            mse_loss = self.mse_calc(target_image, gen_output)
            
        generator_gradients = gen_tape.gradient(gen_loss, self.generator.trainable_variables)
        discriminator_gradients = disc_tape.gradient(dis_loss, self.discriminator.trainable_variables)
        self.generator_optimizer.apply_gradients(zip(generator_gradients, self.generator.trainable_variables))
        self.discriminator_optimizer.apply_gradients(zip(discriminator_gradients, self.discriminator.trainable_variables))
        return gen_loss, dis_loss, mae_loss, mse_loss

    def val_step(self, input_image, target_image):
        gen_output = self.generator(input_image, training=False)
        disc_real_output = self.discriminator([input_image, target_image], training=False)
        disc_generated_output = self.discriminator([input_image, gen_output], training=False)
        gen_loss = self.generator_loss(disc_generated_output, gen_output, target_image)
        dis_loss = self.discriminator_loss(disc_real_output, disc_generated_output)
        mae_loss = self.mae_calc(target_image, gen_output)
        mse_loss = self.mse_calc(target_image, gen_output)
        return gen_loss, dis_loss, mae_loss, mse_loss
    
    def train(
            self, 
            train_data: tuple,
            val_data: tuple = None,
            epochs=10, 
            batch_size=32, 
            monitor="val_mean_absolute_error",
            lrdecay_gen=True,
            lrdecay_dis=False,
            lrdecay_factor_gen=0.1,
            lrdecay_factor_dis=0.1,
            lrdecay_wait_gen=10,
            lrdecay_wait_dis=10,
            reducelr_on_plateau=False,
            reducelr_factor=0.1,
            reducelr_patience=10,
            min_lr=1e-10,
            early_stopping=True,
            early_stopping_patience=32,
            save_ckpt_best=True,
            save_ckpt=True,
            ckpt_interval=1,
            ):

        """
        Train the Pix2Pix model and log all losses including MSE and MAE.
        
        Args:
            train_dataset (tf.data.Dataset): Training dataset yielding (input_image, target_image) pairs.
            val_dataset (tf.data.Dataset): Optional validation dataset yielding (input_image, target_image) pairs.
            checkpoint_pr (str): Prefix for checkpoint files.
            save_interval (int): Interval (in epochs) for saving checkpoints.
            batch_size (int): Batch size for training.
            log_file (str): Filepath to save loss metrics as a CSV file.
        """
        
        print('#'*20, ' GENERATOR ARCHITECTURE ', '#'*20)
        print(self.generator.summary())
        print('#'*20, ' DISCRIMINATOR ARCHITECTURE ', '#'*20)
        print(self.discriminator.summary())
        print(f"Pix2Pix training started for {epochs} epochs ...")
        print(f"Batch size set to {batch_size} ...")

        # -----------------------
        # Build tf.data pipeline
        # -----------------------
        train_dataset, val_dataset = build_tf_data_pipeline(train_data, val_data, batch_size=batch_size, train_shuffle=True)
        
        train_steps = len(train_data[0]) // batch_size
        val_steps = len(val_data[0]) // batch_size

        print(f"Training for {epochs} epochs with {train_steps} steps per epoch.")

        # Initialize the csv logger
        csvlogger = CustomCSVLogger(f"{self.save_path}/{self.expname}_logs.csv")
        
        #########################
        # ITERATE OVER THE EPOCHS
        #########################
        for epoch in range(epochs):
            start_time = time.time()
            print(f"\nEpoch {epoch + 1}/{epochs}")
            
            # ----------------------------
            # Training Loop
            # ----------------------------
            print("Training ...")
            train_gen_loss = train_dis_loss = train_mae_loss = train_mse_loss = 0
            for input_image, target_image in train_dataset.take(train_steps):

                print("Training ...")
                gen_loss, dis_loss, mae_loss, mse_loss = self.train_step(input_image, target_image)
                
                # Accumulate the loss values over train steps
                train_gen_loss += gen_loss.numpy()
                train_dis_loss += dis_loss.numpy()
                train_mae_loss += mae_loss.numpy()
                train_mse_loss += mse_loss.numpy()
               
            # Average the losses over steps
            train_gen_loss /= train_steps
            train_dis_loss /= train_steps
            train_mae_loss /= train_steps
            train_mse_loss /= train_steps

            # Update learning rate if scheduler is enabled
            if lrdecay_gen:
                new_lr = self.lr_scheduler(epoch, self.generator_optimizer.learning_rate, lrdecay_factor_gen, lrdecay_wait_gen)
                self.generator_optimizer.learning_rate.assign(new_lr)  # Update generator optimizer's learning rate
            if lrdecay_dis:
                new_lr = self.lr_scheduler(epoch, self.discriminator_optimizer.learning_rate, lrdecay_factor_dis, lrdecay_wait_dis)
                self.discriminator_optimizer.learning_rate.assign(new_lr)  # Update discriminator optimizer's learning rate

            # ----------------------------
            # Validation Loop
            # ----------------------------
            if val_data is not None:

                print("Validating ...")  # Indicate validation process
                val_gen_loss = val_dis_loss = val_mae_loss = val_mse_loss = 0
                for input_image, target_image in val_dataset.take(val_steps):

                    # Accumulate all the validation losses
                    gen_loss, dis_loss, mae_loss, mse_loss = self.val_step(input_image, target_image)
                    val_gen_loss += gen_loss.numpy()
                    val_dis_loss += dis_loss.numpy()
                    val_mae_loss += mae_loss.numpy()
                    val_mse_loss += mse_loss.numpy()

                # Average the accumulated losses over the validation steps
                val_gen_loss /= val_steps
                val_dis_loss /= val_steps
                val_mae_loss /= val_steps
                val_mse_loss /= val_steps

                # -----------------------
                # Add Training Callbacks
                # -----------------------
                monitored_metric_dict = {
                    "val_generator_loss"     : val_gen_loss,
                    "val_discriminator_loss" : val_dis_loss,
                    "val_mean_absolute_error": val_mae_loss,
                    "val_mean_squared_error" : val_mse_loss,
                    }

                monitored_metric = monitored_metric_dict.get(monitor, None) # Determine monitored metric
                if monitored_metric is None:
                    raise ValueError(f"Unsupported monitor value: {monitor}. Available options: {', '.join(monitored_metric_dict.keys())}")

                # Reduce learning rate on plateau
                if reducelr_on_plateau:
                    self.reduce_lr_on_plateau(monitored_metric, reducelr_factor, reducelr_patience, min_lr)

                # Save best checkpoint
                if save_ckpt_best:
                    if self.save_best_model(monitored_metric):
                        self.generator.save(f"{self.save_path}/{self.expname}_{self.best_gen_suffix}.keras")
                        self.discriminator.save(f"{self.save_path}/{self.expname}_{self.best_dis_suffix}.keras")
                        print(f"\tBest Generator and Discriminator model saved at epoch {epoch + 1}")

                # Early stopping
                if early_stopping and self.early_stopping_check(monitored_metric, early_stopping_patience):
                    print("\tEarly stopping triggered.")
                    break

            else:
                warnings.warn("\tNo validation data provided. Not able to save best model, apply early stopping or reduce learning rate!", UserWarning)

            # ----------------------------
            # Logging Metrics to CSV file
            # ----------------------------
            metrics = {
                "generator_loss"     : train_gen_loss,
                "discriminator_loss" : train_dis_loss,
                "mean_absolute_error": train_mae_loss,
                "mean_squared_error" : train_mse_loss,
            }

            val_metrics = {
                "val_generator_loss"     : val_gen_loss,
                "val_discriminator_loss" : val_dis_loss,
                "val_mean_absolute_error": val_mae_loss,
                "val_mean_squared_error" : val_mse_loss,
            } if val_data is not None else None

            # Log metrics to CSV
            csvlogger.log_metrics(epoch, metrics, val_metrics if val_data is not None else None)

            # Epoch end timing
            epoch_time = time.time() - start_time
            print(f"Epoch {epoch + 1} - Time: {epoch_time:.2f}s")
          
            if save_ckpt and (epoch + 1) % ckpt_interval == 0:
                # Save generator checkpoint at every save_interval epoch
                self.generator.save(f"{self.save_path}/{self.expname}_ckpt/gen_e{epoch+1:03d}.keras")
                print(f"\tGenerator checkpoint saved at epoch {epoch + 1}")
                self.discriminator.save(f"{self.save_path}/{self.expname}_ckpt/dis_e{epoch+1:03d}.keras")
                print(f"\tDiscriminator checkpoint saved at epoch {epoch + 1}")
            
            # Epoch end timing
            wall_time_sec = time.time() - start_time
            self.time_list.append(wall_time_sec)

            # Log metrics to TensorBoard
            if self.log_tensorboard:
                with self.summary_writer.as_default():
                    tf.summary.scalar('generator_loss', train_gen_loss, step=epoch)
                    tf.summary.scalar('discriminator_loss', train_dis_loss, step=epoch)
                    tf.summary.scalar('mean_absolute_error', train_mae_loss, step=epoch)
                    tf.summary.scalar('mean_squared_error', train_mse_loss, step=epoch)
                    if val_data is not None:
                        tf.summary.scalar('val_generator_loss', val_gen_loss, step=epoch)
                        tf.summary.scalar('val_discriminator_loss', val_dis_loss, step=epoch)
                        tf.summary.scalar('val_mean_absolute_error', val_mae_loss, step=epoch)
                        tf.summary.scalar('val_mean_squared_error', val_mse_loss, step=epoch)
                    tf.summary.scalar('epoch_time', wall_time_sec, step=epoch)  # Log epoch time

            # ---------------------------------------------
            # Display the training and validation progress
            # ---------------------------------------------
            if val_data is None:
                table = [
                        ["Generator Loss",     f"{train_gen_loss:.4f}"],
                        ["Discriminator Loss", f"{train_dis_loss:.4f}"],
                        ["MAE Loss",           f"{train_mae_loss:.4f}"],
                        ["MSE Loss",           f"{train_mse_loss:.4f}"],
                        ]
                # Print as table
                print(tabulate(table,  tablefmt="pretty", 
                               headers=["Metric", "Training"], 
                               colalign=("left", "center"))
                               ) 
            else:
                table = [
                        ["Generator Loss",     f"{train_gen_loss:.4f}",  f"{val_gen_loss:.4f}"],
                        ["Discriminator Loss", f"{train_dis_loss:.4f}", f"{val_dis_loss:.4f}"],
                        ["MAE Loss",           f"{train_mae_loss:.4f}",  f"{val_mae_loss:.4f}"],
                        ["MSE Loss",           f"{train_mse_loss:.4f}",  f"{val_mse_loss:.4f}"],
                        ]
                # Print as table
                print(tabulate(table, tablefmt="pretty", 
                               headers=["Metric", "Training", "Validation"] , 
                               colalign=("left", "center", "center"))
                               ) 
            print(f"Time: {wall_time_sec:.2f}s")
    
    def plot_training_curves(self, plot_title=None):
        """
        Function to plot training curves for various metrics including generator and discriminator losses.
        """
        self._load_trainlogs()

        # Create subplots: 2 rows and 2 columns to accommodate 4 plots
        fig, axs = plt.subplots(2, 2, figsize=(12, 12))  # Adjusting the layout for 2x2 subplots
        plt.subplots_adjust(bottom=0.2, wspace=0.3)

        # Set the main title of the plot
        fig.suptitle(plot_title if plot_title is not None else self.expname, fontsize=30, fontfamily='serif', fontweight='bold')

        # Plot the different metrics on the subplots
        plot_traincurve(self.trainlogs, ax=axs[0, 0], header='generator_loss')
        plot_traincurve(self.trainlogs, ax=axs[0, 1], header='discriminator_loss')
        plot_traincurve(self.trainlogs, ax=axs[1, 0], header='mean_absolute_error') 
        plot_traincurve(self.trainlogs, ax=axs[1, 1], header='mean_squared_error')

        # Add a legend for the plots
        fig.legend(["Training", "Validation", "Min.Val."], loc='lower center', ncol=3, fontsize=16)

        # Save the plot as a .jpg file
        save_fig_as = f"{self.save_path}/{self.expname}_traincurve.jpg"
        plt.savefig(save_fig_as, format='jpg', dpi=400, bbox_inches='tight')
        print(f"Training curves saved as {save_fig_as}")
