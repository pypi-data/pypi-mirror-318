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

# ------------------------------------------------
# The SRGAN class for GAN Training and Validation
# ------------------------------------------------    
class SRGAN(ModelTraining):
    
    def __init__(
            self, 
            prefix: str='tst',  
            save_path: str='.',
            generator=None, 
            discriminator=None, 
            gen_lr_init=2e-4,
            dis_lr_init=2e-4,
            extract_features=False, 
            feature_extractor='VGG19',  
            output_layer='block3_conv4', 
            pretrained_weights="imagenet",
            cl_opt='WMAE',
            lambda_value=1e-3,
            log_tensorboard = False,
            enable_function=True,
            suffix=None,
            ):
        # Initialize the parent class (ModelTraining)
        super().__init__(prefix, save_path, log_tensorboard=log_tensorboard, enable_function=enable_function, suffix=suffix)
        
        # Set specific parameters for SRGAN
        self.generator = generator
        self.discriminator = discriminator
        
        # Content loss parameters
        self.cl_opt = cl_opt
        self.lambda_value = lambda_value
        self.extract_features=extract_features, 
        self.feature_extractor=feature_extractor,  
        self.output_layer=output_layer, 
        self.pretrained_weights=pretrained_weights

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
       return (f"SRGAN Configuration:\n"
               f"  Exp.Name: {self.expname}\n"
               f"  Output Save Directory: {self.save_path}\n"
               f"  Content Loss Option: {self.cl_opt}\n"
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
    
    def generator_loss(self, gen_output):
        return self.bce_loss(tf.ones_like(gen_output), gen_output)
    
    def content_loss(self, target, gen_output):
        """
        Computes the content loss between the target and generated output.

        Parameters:
            target (tf.Tensor): Ground truth tensor.
            gen_output (tf.Tensor): Generated output tensor from the model.
            extract_features (bool): Whether to extract features using a pre-trained model.
            feature_extractor (str or tf.keras.Model): Feature extraction model ('VGG19' or a custom model).
            output_layer (str): Layer name from which features are extracted (used for 'VGG19').
            weights_path (str): Path to pre-trained weights ('imagenet' for default ImageNet weights or custom path).

        Returns:
            tf.Tensor: Content loss value.
        """
        
        if self.extract_features: # If feature extraction is required  
            if self.feature_extractor == 'VGG19': # Load the feature extractor model
                # Use VGG19 as the feature extractor
                vgg19 = tf.keras.applications.VGG19(weights=self.pretrained_weights, include_top=False)
                feature_extractor_ = tf.keras.Model(
                    inputs=vgg19.input,
                    outputs=vgg19.get_layer(self.output_layer).output
                )
                # Preprocess inputs for VGG19
                target = tf.keras.applications.vgg19.preprocess_input(tf.repeat(target, repeats=3, axis=-1))
                gen_output = tf.keras.applications.vgg19.preprocess_input(tf.repeat(gen_output, repeats=3, axis=-1))
            elif isinstance(self.feature_extractor, tf.keras.Model):
                # Custom feature extractor is provided
                feature_extractor_ = self.feature_extractor 
            else:
                raise ValueError(f"Invalid feature_extractor: {self.feature_extractor}. Must be 'VGG19' or a tf.keras.Model.")

            # Extract features from target and generated output
            target = feature_extractor_(target)
            gen_output = feature_extractor_(gen_output)

        # Compute the loss based on the selected option
        if self.cl_opt == 'WMAE':  # Weighted Mean Absolute Error
            return weighted_mae(target, gen_output)
        elif self.cl_opt == 'MAE':  # Mean Absolute Error
            return self.mae_calc(target, gen_output)
        elif self.cl_opt == 'WMSE':  # Weighted Mean Squared Error
            return weighted_mse(target, gen_output)
        elif self.cl_opt == 'MSE':  # Mean Squared Error
            return self.mse_calc(target, gen_output)
        else:
            raise ValueError(
                f"Invalid cl_opt value: {self.cl_opt}. Expected one of 'WMAE', 'MAE', 'WMSE', 'MSE'."
            )
        
    def train_step(self, input_image, target_image): 

        """
        SRGAN training step.
        Takes an LR and an HR image batch as input and returns the computed perceptual loss and discriminator loss.
        """
        with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:

            # Forward pass
            gen_output = self.generator(input_image, training=True)
            disc_real_output = self.discriminator(target_image, training=True)
            disc_generated_output = self.discriminator(gen_output, training=True)

            # Compute losses
            gen_loss = self.generator_loss(disc_generated_output)
            dis_loss = self.discriminator_loss(disc_real_output, disc_generated_output)
            cnt_loss = self.content_loss(target_image, gen_output)
            prc_loss = cnt_loss + self.lambda_value * gen_loss
            mse_loss = self.mse_calc(target_image, gen_output)
            mae_loss = self.mae_calc(target_image, gen_output)

        # Compute gradient of perceptual loss w.r.t. generator weights 
        generator_gradients = gen_tape.gradient(prc_loss, self.generator.trainable_variables)
        # Compute gradient of discriminator loss w.r.t. discriminator weights 
        discriminator_gradients = disc_tape.gradient(dis_loss, self.discriminator.trainable_variables)

        # Update weights of generator and discriminator
        self.generator_optimizer.apply_gradients(zip(generator_gradients, self.generator.trainable_variables))
        self.discriminator_optimizer.apply_gradients(zip(discriminator_gradients, self.discriminator.trainable_variables))

        return gen_loss, dis_loss, cnt_loss, prc_loss, mae_loss, mse_loss
    
    def val_step(self, input_image, target_image):
        """
        SRGAN validation step.
        Takes an LR and an HR image batch as input and returns the computed perceptual loss and discriminator loss.
        """
        # Forward pass in inference mode
        gen_output = self.generator(input_image, training=False)
        disc_real_output = self.discriminator(target_image, training=False)
        disc_generated_output = self.discriminator(gen_output, training=False)

        # Compute losses
        gen_loss = self.generator_loss(disc_generated_output)
        dis_loss = self.discriminator_loss(disc_real_output, disc_generated_output)
        cnt_loss = self.content_loss(target_image, gen_output)
        prc_loss = cnt_loss + self.lambda_value * gen_loss
        mse_loss = self.mse_calc(target_image, gen_output)
        mae_loss = self.mae_calc(target_image, gen_output)

        return gen_loss, dis_loss, cnt_loss, prc_loss, mae_loss, mse_loss

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
        Train the SRGAN model and log all losses including MSE and MAE.
        """
        
        print('#'*20, ' GENERATOR ARCHITECTURE ', '#'*20)
        print(self.generator.summary())
        print('#'*20, ' DISCRIMINATOR ARCHITECTURE ', '#'*20)
        print(self.discriminator.summary())
        print(f"SRGAN training started for {epochs} epochs ...")
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
            train_gen_loss = train_dis_loss = train_cnt_loss =  train_prc_loss = train_mae_loss = train_mse_loss = 0
            for input_image, target_image in train_dataset.take(train_steps):
                
                gen_loss, dis_loss, cnt_loss, prc_loss, mae_loss, mse_loss = self.train_step(input_image, target_image)

                # Accumulate the loss values over train steps
                train_gen_loss += gen_loss.numpy()
                train_dis_loss += dis_loss.numpy()
                train_cnt_loss += cnt_loss.numpy()
                train_prc_loss += prc_loss.numpy()
                train_mae_loss += mae_loss.numpy()
                train_mse_loss += mse_loss.numpy()
                
            # Average the losses over steps
            train_gen_loss /= train_steps
            train_dis_loss /= train_steps
            train_cnt_loss /= train_steps
            train_prc_loss /= train_steps
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
                val_gen_loss = val_dis_loss = val_cnt_loss = val_prc_loss= val_mae_loss = val_mse_loss = 0
                for input_image, target_image in val_dataset.take(val_steps):
                    gen_loss, dis_loss, cnt_loss, prc_loss, mae_loss, mse_loss = self.val_step(input_image, target_image)
                    val_gen_loss += gen_loss.numpy()
                    val_dis_loss += dis_loss.numpy()
                    val_cnt_loss += cnt_loss.numpy()
                    val_prc_loss += prc_loss.numpy()
                    val_mae_loss += mae_loss.numpy()
                    val_mse_loss += mse_loss.numpy()

                # Average the accumulated losses over the validation steps
                val_gen_loss /= val_steps
                val_dis_loss /= val_steps
                val_cnt_loss /= val_steps
                val_prc_loss /= val_steps
                val_mae_loss /= val_steps
                val_mse_loss /= val_steps

                # -----------------------
                # Add Training Callbacks
                # -----------------------
                monitored_metric_dict = {
                    "val_generator_loss"     : val_gen_loss,
                    "val_discriminator_loss" : val_dis_loss,
                    "val_content_loss"       : val_cnt_loss,
                    "val_perceptual_loss"    : val_prc_loss,
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
            
            # ----------------------
            # Logging Metrics
            # ----------------------
            metrics = {
                "generator_loss"     : train_gen_loss,
                "discriminator_loss" : train_dis_loss,
                "content_loss"       : train_cnt_loss,
                "perceptual_loss"    : train_prc_loss,
                "mean_absolute_error": train_mae_loss,
                "mean_squared_error" : train_mse_loss,
            }

            val_metrics = {
                "val_generator_loss"     : val_gen_loss,
                "val_discriminator_loss" : val_dis_loss,
                "val_content_loss"       : val_cnt_loss,
                "val_perceptual_loss"    : val_prc_loss,
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

            # Log metrics to TensorBoard
            if self.log_tensorboard:
                with self.summary_writer.as_default():
                    tf.summary.scalar('generator_loss',      train_gen_loss, step=epoch)
                    tf.summary.scalar('discriminator_loss',  train_dis_loss, step=epoch)
                    tf.summary.scalar('content_loss',        train_cnt_loss, step=epoch)
                    tf.summary.scalar('perceptual_loss',     train_prc_loss, step=epoch)
                    tf.summary.scalar('mean_absolute_error', train_mae_loss, step=epoch)
                    tf.summary.scalar('mean_squared_error',  train_mse_loss, step=epoch) 
                    if val_data is not None:
                        tf.summary.scalar('val_generator_loss',      val_gen_loss, step=epoch)
                        tf.summary.scalar('val_discriminator_loss',  val_dis_loss, step=epoch)
                        tf.summary.scalar('val_content_loss',        val_cnt_loss, step=epoch)
                        tf.summary.scalar('val_perceptual_loss',     val_prc_loss, step=epoch)
                        tf.summary.scalar('val_mean_absolute_error', val_mae_loss, step=epoch)
                        tf.summary.scalar('val_mean_squared_error',  val_mse_loss, step=epoch)    
                    tf.summary.scalar('epoch_time', wall_time_sec, step=epoch)  # Log epoch time

           # Epoch end timing
            wall_time_sec = time.time() - start_time
            self.time_list.append(wall_time_sec)

            # ---------------------------------------------
            # Display the training and validation progress
            # ---------------------------------------------
            
            if val_data is None:
                table = [
                        ["Generator Loss",     f"{train_gen_loss:.4f}"],
                        ["Discriminator Loss", f"{train_dis_loss:.4f}"],
                        ["Content Loss",       f"{train_cnt_loss:.4f}"],
                        ["Perceptual Loss",    f"{train_prc_loss:.4f}"],
                        ["MSE Loss",           f"{train_mse_loss:.4f}"],
                        ["MAE Loss",           f"{train_mae_loss:.4f}"],
                        ]
                # Print as table
                print(tabulate(table,  tablefmt="pretty", 
                               headers=["Metric", "Training"], 
                               colalign=("left", "center"))
                               ) 
            else:
                table = [
                        ["Generator Loss",     f"{train_gen_loss:.4f}", f"{val_gen_loss:.4f}"],
                        ["Discriminator Loss", f"{train_dis_loss:.4f}", f"{val_dis_loss:.4f}"],
                        ["Content Loss",       f"{train_cnt_loss:.4f}", f"{val_cnt_loss:.4f}"],
                        ["Perceptual Loss",    f"{train_prc_loss:.4f}", f"{val_prc_loss:.4f}"],
                        ["MAE Loss",           f"{train_mae_loss:.4f}", f"{val_mae_loss:.4f}"],
                        ["MSE Loss",           f"{train_mse_loss:.4f}", f"{val_mse_loss:.4f}"],
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
        fig, axs = plt.subplots(3, 2, figsize=(12, 18))  # Adjusting the layout for 2x2 subplots
        plt.subplots_adjust(bottom=0.2, wspace=0.3)

        # Set the main title of the plot
        fig.suptitle(plot_title if plot_title is not None else self.expname, fontsize=30, fontfamily='serif', fontweight='bold')

        # Plot the different metrics on the subplots
        plot_traincurve(self.trainlogs, ax=axs[0, 0], header='generator_loss')
        plot_traincurve(self.trainlogs, ax=axs[0, 1], header='discriminator_loss')
        plot_traincurve(self.trainlogs, ax=axs[1, 0], header='content_loss')
        plot_traincurve(self.trainlogs, ax=axs[1, 1], header='perceptual_loss')
        plot_traincurve(self.trainlogs, ax=axs[2, 0], header='mean_absolute_error') 
        plot_traincurve(self.trainlogs, ax=axs[2, 1], header='mean_squared_error')

        # Add a legend for the plots
        fig.legend(["Training", "Validation", "Min.Val."], loc='lower center', ncol=3, fontsize=16)

        # Save the plot as a .jpg file
        save_fig_as = f"{self.save_path}/{self.expname}_traincurve.jpg"
        plt.savefig(save_fig_as, format='jpg', dpi=400, bbox_inches='tight')
        print(f"Training curves saved as {save_fig_as}")