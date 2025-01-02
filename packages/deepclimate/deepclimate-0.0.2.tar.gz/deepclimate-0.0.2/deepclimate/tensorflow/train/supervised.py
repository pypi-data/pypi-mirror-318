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

# ------------------------------------------------
# The ModelTraining class for Supervised Learning 
# ------------------------------------------------
class ModelTraining:
    
    def __init__(
            self,
            prefix: str='tst', 
            save_path: str='.',
            generator=None,
            loss_fn=None,
            lr_init = 1e-4,
            log_tensorboard = True,
            enable_function=True,
            suffix = None,
            ):
        
        self.expname = f"{prefix}_{suffix}" if suffix is not None else f"{prefix}"
        self.save_path = save_path
        
        # Attribute model params
        self.generator = generator
        self.loss_fn = loss_fn
        self.lr_init = lr_init
        self.log_tensorboard = log_tensorboard # FLAG
        
        # Initialize TensorBoard summary writer
        if self.log_tensorboard:
            # Directory to store TensorBoard logs
            self.tensorboard_log_dir = f'{self.save_path}/{self.expname}_logs/{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}'  
            self.summary_writer = tf.summary.create_file_writer(self.tensorboard_log_dir)
            
        self.enable_function = enable_function   
        self.best_model = None
        self.best_gen_suffix, self.best_dis_suffix= 'ckpt_best_gen', 'ckpt_best_dis'
        self.trainlogs = None
        self.best_val_metric = float('inf')
        self.early_stop_counter = self.reduce_lr_counter = 0 
        self.time_list = []

        self.generator_optimizer = tf.keras.optimizers.Adam(lr_init)
        self.mse_calc = tf.keras.losses.MeanSquaredError()
        self.mae_calc = tf.keras.losses.MeanAbsoluteError()
        
        if self.enable_function:
            self.train_step = tf.function(self.train_step)
        
        # Create empty directory to save models
        gen_models_dir = f"{self.save_path}/{self.expname}_ckpt"
        if not os.path.exists(gen_models_dir):
            os.makedirs(gen_models_dir)
        
        if generator:
            print(
                f"\nModel training initialized with:\n"
                f"  - Generator: {self.generator.name}\n"
                f"  - Learning Rates:\n"
                f"      Generator: {lr_init}\n"
            )

    def train_step(self, input_image, target_image):
        with tf.GradientTape() as tape:  # Start gradient tape for tracking the gradients
            predictions = self.generator(input_image, training=True)  # Forward pass through the generator
            gen_loss = self.loss_fn(target_image, predictions)  # Compute training loss (tracked by tape)
            mae_loss = self.mae_calc(target_image, predictions)  # Compute Mean Absolute Error (tracked by tape)
            mse_loss = self.mse_calc(target_image, predictions)  # Compute Mean Squared Error (tracked by tape)

        # Compute gradients with respect to model variables (tracked by tape)
        gradients = tape.gradient(gen_loss, self.generator.trainable_variables)
        # Apply gradients to update model variables (not tracked by tape)
        self.generator_optimizer.apply_gradients(zip(gradients, self.generator.trainable_variables))
        
        return gen_loss, mae_loss, mse_loss  # Return the computed loss and metrics
    
    def val_step(self, input_image, target_image):
        predictions = self.generator(input_image, training=False)             
        gen_loss = self.loss_fn(target_image, predictions)
        mae_loss = self.mae_calc(target_image, predictions)
        mse_loss = self.mse_calc(target_image, predictions)
        
        return gen_loss, mae_loss, mse_loss

    def early_stopping_check(self, monitored_metric, early_stopping_patience, mode="min"):
        if (mode == "min" and monitored_metric < self.best_val_metric) or \
        (mode == "max" and monitored_metric > self.best_val_metric):  # Check for improvement
            self.best_val_metric = monitored_metric  # Update the best monitored metric
            self.early_stop_counter = 0  # Reset early stopping counter
        else:
            self.early_stop_counter += 1  # Increment early stopping counter if no improvement

        # Early stopping check: Stop training if there's no improvement for 'patience' epochs
        if self.early_stop_counter >= early_stopping_patience:
            print(f"\nEarly stopping. No improvement in monitored metric for {self.early_stop_counter} consecutive epochs.")
            return True
        return False

    def save_best_model(self, monitored_metric, mode="min"):
        if (mode == "min" and monitored_metric < self.best_val_metric) or \
        (mode == "max" and monitored_metric > self.best_val_metric):  # Check for improvement
            self.best_val_metric = monitored_metric  # Update the best monitored metric
            return True
        else:
            return False

    def reduce_lr_on_plateau(self, monitored_metric, reducelr_factor, reducelr_patience, min_lr, mode="min"):
        if (mode == "min" and monitored_metric >= self.best_val_metric) or \
        (mode == "max" and monitored_metric <= self.best_val_metric):  # No improvement in metric
            self.reduce_lr_counter += 1
            print(f"\tMonitored metric did not improve. ReduceLR counter: {self.reduce_lr_counter}/{reducelr_patience}")

            if self.reduce_lr_counter >= reducelr_patience:  # If patience is exceeded, reduce learning rate
                old_lr = self.generator_optimizer.learning_rate.numpy()
                new_lr = max(old_lr * reducelr_factor, min_lr)  # Ensure it doesn't go below min_lr
                self.generator_optimizer.learning_rate.assign(new_lr)  # Update learning rate
                print(f"\tReduceLROnPlateau: Reducing learning rate for generator: {old_lr:.6f} → {new_lr:.6f}")
                self.reduce_lr_counter = 0  # Reset counter after LR adjustment
        else:
            self.best_val_metric = monitored_metric  # Update best validation loss/metric
            self.reduce_lr_counter = 0  # Reset patience counter

    def lr_scheduler(self, epoch, lr, lrdecay_factor, lrdecay_wait):
        if epoch < lrdecay_wait:
            print(f"\tLR Scheduler: Not activated for epoch {epoch + 1}")
            return lr  # Return the current learning rate without changes
        else:
            # Apply exponential decay
            decay_factor = tf.math.exp(-lrdecay_factor).numpy()  # Compute the decay factor
            new_lr = lr * decay_factor  # Update the learning rate
            print(f"\tLR Scheduler: Updated learning rate: {new_lr:.6f}")
            return new_lr  # Return the updated learning rate

    def train(
            self, 
            train_data: tuple,
            val_data: tuple = None,
            epochs=10, 
            batch_size=32, 
            monitor="val_mean_absolute_error",
            lrdecay_scheduler=True,
            lrdecay_factor=0.1,
            lrdecay_wait=10,
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
        Train the tf.keras.models.Model and log all losses including MSE and MAE.
        
        Args:
            train_data (tuple): Training data as (inputs, targets).
            val_data (tuple, optional): Validation data as (inputs, targets). Default is None.
            ...
        """
        print('#' * 20, ' GENERATOR ARCHITECTURE ', '#' * 20)
        print(self.generator.summary())
        print(f"Model training started for {epochs} epochs ...")
        print(f"Batch size set to {batch_size} ...")

        # Build data pipelines
        train_dataset, val_dataset = build_tf_data_pipeline(train_data, val_data, batch_size=batch_size, train_shuffle=True)
        train_steps = len(train_data[0]) // batch_size
        val_steps = len(val_data[0]) // batch_size if val_data else 0

        print(f"Training for {epochs} epochs with {train_steps} steps per epoch.")

        # Initialize CSV logger
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
            train_gen_loss = train_mse_loss = train_mae_loss = 0
            for input_image, target_image in train_dataset.take(train_steps):
                gen_loss, mae_loss, mse_loss = self.train_step(input_image, target_image)
                train_gen_loss += gen_loss.numpy()
                train_mse_loss += mse_loss.numpy()
                train_mae_loss += mae_loss.numpy()

            # Average training losses
            train_gen_loss /= train_steps
            train_mse_loss /= train_steps
            train_mae_loss /= train_steps

            # Update learning rate if scheduler is enabled
            if lrdecay_scheduler:
                new_lr = self.lr_scheduler(epoch, self.generator_optimizer.learning_rate, lrdecay_factor, lrdecay_wait)
                self.generator_optimizer.learning_rate.assign(new_lr)  # Update optimizer's learning rate

            # ----------------------------
            # Validation Loop
            # ----------------------------
            if val_data is not None:
                
                print("Validating ...")
                val_gen_loss = val_mse_loss = val_mae_loss = 0
                for input_image, target_image in val_dataset.take(val_steps):
                    gen_loss, mae_loss, mse_loss = self.val_step(input_image, target_image)
                    val_gen_loss += gen_loss.numpy()
                    val_mse_loss += mse_loss.numpy()
                    val_mae_loss += mae_loss.numpy()

                # Average validation losses
                val_gen_loss /= val_steps
                val_mse_loss /= val_steps
                val_mae_loss /= val_steps

                # -----------------------
                # Add Training Callbacks
                # -----------------------
                monitored_metric_dict = {
                    "val_loss": val_gen_loss,
                    "val_mean_absolute_error": val_mae_loss,
                    "val_mean_squared_error": val_mse_loss,
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
                        print(f"\tBest Generator model saved at epoch {epoch + 1}")

                # Early stopping
                if early_stopping and self.early_stopping_check(monitored_metric, early_stopping_patience):
                    print("\tEarly stopping triggered.")
                    break

            else:
                warnings.warn("\tNo validation data provided. Skipping validation-dependent callbacks.", UserWarning)

            # End of epoch logging
            print(f"Epoch {epoch + 1} completed in {time.time() - start_time:.2f}s.")

            # ----------------------
            #    Logging Metrics
            # ----------------------
            metrics = {
                "loss": train_gen_loss,
                "mean_absolute_error": train_mae_loss,
                "mean_squared_error": train_mse_loss,
            }

            val_metrics = {
                "val_loss": val_gen_loss,
                "val_mean_absolute_error": val_mae_loss,
                "val_mean_squared_error": val_mse_loss,
            } if val_data is not None else None

            # Log metrics to CSV
            csvlogger.log_metrics(epoch, metrics, val_metrics if val_data is not None else None)

            # Epoch end timing
            epoch_time = time.time() - start_time
            print(f"Epoch {epoch + 1} - Time: {epoch_time:.2f}s")
            
            # Save all models
            if save_ckpt and (epoch + 1) % ckpt_interval == 0:
                # Save generator checkpoint at every save_interval epoch
                self.generator.save(f"{self.save_path}/{self.expname}_ckpt/gen_e{epoch+1:03d}.keras")
                print(f"\tGenerator checkpoint saved at epoch {epoch + 1}")
            
            # Epoch end timing
            wall_time_sec = time.time() - start_time
            self.time_list.append(wall_time_sec)

            # Log metrics to TensorBoard
            if self.log_tensorboard:
                with self.summary_writer.as_default():
                    tf.summary.scalar('loss', train_gen_loss, step=epoch)
                    tf.summary.scalar('mean_squared_error', train_mse_loss, step=epoch)
                    tf.summary.scalar('mean_absolute_error', train_mae_loss, step=epoch)
                    if val_data is not None:
                        tf.summary.scalar('val_loss', val_gen_loss, step=epoch)
                        tf.summary.scalar('val_mean_squared_error', val_mse_loss, step=epoch)
                        tf.summary.scalar('val_mean_absolute_error', val_mae_loss, step=epoch)
                    tf.summary.scalar('epoch_time', wall_time_sec, step=epoch)  # Log epoch time

            # ---------------------------------------------
            # Display the training and validation progress
            # ---------------------------------------------    
            if val_data is None:
                table = [
                        ["Generator Loss", f"{train_gen_loss:.4f}"],
                        ["MSE Loss",       f"{train_mse_loss:.4f}"],
                        ["MAE Loss",       f"{train_mae_loss:.4f}"],
                        ]
                # Print as table
                print(tabulate(table,  tablefmt="pretty", 
                               headers=["Metric", "Training"], 
                               colalign=("left", "center"))
                               ) 
            else:
                table = [
                        ["Generator Loss", f"{train_gen_loss:.4f}", f"{val_gen_loss:.4f}"],
                        ["MSE Loss", f"{train_mse_loss:.4f}",       f"{val_mse_loss:.4f}"],
                        ["MAE Loss", f"{train_mae_loss:.4f}",       f"{val_mae_loss:.4f}"],
                        ]
                # Print as table
                print(tabulate(table, tablefmt="pretty", 
                               headers=["Metric", "Training", "Validation"] , 
                               colalign=("left", "center", "center"))
                               ) 
            print(f"Time: {wall_time_sec:.2f}s")
        
    def train_by_fit(
            self, 
            train_data: tuple,
            val_data: tuple = None,
            epochs=10, 
            batch_size=32, 
            monitor="val_mean_absolute_error",
            lrdecay_scheduler=True,
            lrdecay_factor=0.1,
            lrdecay_wait=10,
            reducelr_on_plateau=False,
            reducelr_factor=0.1,
            reducelr_patience=10,
            min_lr=1e-10,
            early_stopping=True,
            early_stopping_patience=32,
            save_ckpt_best=True,
            save_ckpt=True,
            ):
        
        """To  train the compiled tf.keras.models.Model objects"""
        
        # -----------------------
        # Build tf.data pipeline
        # -----------------------
        train_dataset, val_dataset = build_tf_data_pipeline(train_data, val_data, batch_size=batch_size, train_shuffle=True)

        # ----------------------------
        # Compile the tf.models.Model
        # ----------------------------     
        self.generator.compile(optimizer=tf.keras.optimizers.Adam(self.lr_init),
                        loss=self.loss_fn,
                        metrics=[tf.keras.losses.MeanAbsoluteError(), 
                                tf.keras.losses.MeanSquaredError(),
                                ]
                        ) 
        
        # -----------------------------------
        # Define mandatory training callbacks
        # -----------------------------------
        logs_csv_path = f"{self.save_path}/{self.expname}_logs.csv"
        csv_logger = tf.keras.callbacks.CSVLogger(logs_csv_path, append=True)

        callbacks_list = [csv_logger] # Default Callback List

        # -----------------------------------
        # Define optional training callbacks
        # -----------------------------------

        if save_ckpt:

            model_save_dir = f"{self.save_path}/{self.expname}_ckpt/gen_e{{epoch:03d}}.keras"
            model_save_callback = tf.keras.callbacks.ModelCheckpoint(filepath=model_save_dir,
                                                                    save_weights_only=False,
                                                                    monitor=monitor,
                                                                    mode= 'min',
                                                                    save_best_only=False)
            callbacks_list.append(model_save_callback)
            
        if save_ckpt_best:
            best_model_path = f"{self.save_path}/{self.expname}_{self.best_gen_suffix}.keras"
            best_model_callback = tf.keras.callbacks.ModelCheckpoint(filepath=best_model_path,
                                                                    save_weights_only=False,
                                                                    monitor=monitor,
                                                                    mode= 'min',
                                                                    save_best_only=True)
            callbacks_list.append(best_model_callback)
        
        if lrdecay_scheduler:
            lr_scheduler_callback = tf.keras.callbacks.LearningRateScheduler(
                lambda epoch, lr: self.lr_scheduler(epoch, lr, lrdecay_factor, lrdecay_wait)) 
            callbacks_list.append(lr_scheduler_callback)
        
        if reducelr_on_plateau:
            reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor=monitor, factor=reducelr_factor, patience=reducelr_patience, min_lr=min_lr)
            callbacks_list.append(reduce_lr)
        
        if early_stopping:
            early_stop = tf.keras.callbacks.EarlyStopping(monitor=monitor, mode= 'min', 
                                                          patience=early_stopping_patience, 
                                                          restore_best_weights=True)
            callbacks_list.append(early_stop)
 
        if self.log_tensorboard:
            tensorboard = tf.keras.callbacks.TensorBoard(log_dir=self.tensorboard_log_dir,
                                                         histogram_freq=1, 
                                                        #profile_batch = '0,20'
                                                         )
            callbacks_list.append(tensorboard)
        
        # Print all details
        print('*'*100)
        print(f"Exp.Name: {self.expname}")
        print('#'*20, ' GENERATOR ARCHITECTURE ', '#'*20)
        print(self.generator.summary())
        print(f"Model training started for {epochs} epochs ...")
        print(f"Batch size set to {batch_size} ...")
        print(f"\nModel name: {self.generator.name}")
        print(f"Training with the Loss fn.: {self.generator.loss}")
        print(f"Initial learning rate set to {self.generator.optimizer.learning_rate.numpy()}")
        print('*'*100)
        print("...MODEL TRAINING STARTS NOW...")
        
        self.generator.fit(
            train_dataset,
            epochs=epochs, 
            verbose=2,
            validation_data=val_dataset, 
            callbacks=callbacks_list,
            ) 

    def _load_trainlogs(self):
        if self.trainlogs is None:  # Only load the model once
            csv_path = f"{self.save_path}/{self.expname}_logs.csv"
            print(f"\nLoading csv file from {csv_path} ...")
            if os.path.exists(csv_path):
                self.trainlogs = pd.read_csv(csv_path)
                return True
            else:
                print(f"CSV file not found at {csv_path}.")
                return False 
            
    def _load_best_model(self):
        if self.best_model is None:  # Only load the model once
            best_model_path = f"{self.save_path}/{self.expname}_{self.best_gen_suffix}.keras" # Edit here
            print(f"\nLoading best model from {best_model_path} ...")
            if os.path.exists(best_model_path):
                self.best_model = tf.keras.models.load_model(best_model_path, compile=False)
                return True
            else:
                print(f"Best model file not found at {best_model_path}.")
                return False 

    def generate_data_and_builf_netcdf(
            self, 
            X_test, 
            model_path: str = None, 
            refd_path: str = 'path_to_ref_data.nc', 
            isgammaloss = False, 
            gamma_thres = 0.5, 
            batch_size = 32, 
            save_raw_npy = False, 
            build_netcdf = True, 
            varname = 'varname', 
            start_date = "YYYY-MM-DD", 
            end_date = "YYYY-MM-DD", 
            tag = None
        ):
        """
        Generates predictions, optionally saves them as npy, and builds a NetCDF file.
        
        Args:
            X_test: Test data for generating predictions.
            model_path: Path to the model file for generating predictions. If None, uses the best model.
            ref_ds: Reference dataset for NetCDF generation (required if `build_netcdf` is True).
            isgammaloss: Whether to use gamma loss for prediction.
            gamma_thres: Threshold for gamma loss.
            batch_size: Batch size for prediction.
            save_raw_npy: Whether to save raw predictions as an npy file.
            build_netcdf: Whether to build a NetCDF file from the predictions.
            varname: Variable name for NetCDF (e.g., 'prec').
            start_date: Start date for NetCDF time dimension.
            end_date: End date for NetCDF time dimension.
            tag: Optional tag identifier for file naming.
        
        Returns:
            gen_data: Generated predictions.
        """
        
        print(f"\nLoading test data inputs for {self.expname}...")

        # Log shapes of input data
        if isinstance(X_test, (list, tuple)) and len(X_test) > 1:
            print(f"X_test shape: {X_test.shape}")
            print(f"S_test shape: {X_test.shape}")
        else:
            print(f"X_test shape: {X_test.shape}")

        # Load the best model if no model path is provided
        if model_path is None:
            FLAG = self._load_best_model()
            if FLAG:
                print(f"Generating best model test data for {self.expname}...")
                # Generate predictions in batches
                gen_data = make_predictions(self.best_model, X_test, batch_size=batch_size, isgammaloss=isgammaloss, thres=gamma_thres)
            else:
                warnings.warn("Best generator file not found! Skipping data generation!", UserWarning)
                return None
        else:
            print(f"Generating test data from {model_path}...")
            gen_data = make_predictions(model_path, X_test, batch_size=batch_size, isgammaloss=isgammaloss, thres=gamma_thres)

        # Save raw predictions as npy if required
        if save_raw_npy:
            filename_suffix = f"{tag}_out_raw" if tag is not None else "out_raw"
            output_path = f"{self.save_path}/{self.expname}_{filename_suffix}_{start_date[:4]}_{end_date[:4]}.npy"
            np.save(output_path, gen_data)
            print(f"Saved raw predictions to {output_path}")

        # Build NetCDF if required
        if build_netcdf:

            # Check if the reference dataset path exists
            if not os.path.exists(refd_path):
                raise FileNotFoundError(f"The reference dataset path '{refd_path}' does not exist.")
            else:
                ref_ds = xr.open_dataset(refd_path)

            clean_array = negtozero(r_logtrans(gen_data))
            filename_suffix = f"{tag}_out" if tag else "out"
            build_netcdf_from_array(
                array=clean_array,
                ref_ds=ref_ds,
                varname=varname,
                start_date=start_date,
                end_date=end_date,
                save_dir=self.save_path,
                filename=f"{self.expname}_{filename_suffix}_{start_date[:4]}_{end_date[:4]}.nc",
            )

        return gen_data
    
    # def evaluations_on_test(self, X_test, y_test, isgammaloss=False):
    #     """
    #     Evaluate the model on the test set.
    #     """
    #     self._load_best_model()
    #     y_pred_raw = make_predictions(X_test, isgammaloss=isgammaloss)
    #     y_pred = r_logtrans(negtozero(y_pred_raw))         # Transform predictions before evaluation
    #     metrics_df = compute_metrics(y_pred.flatten(), y_test.flatten())
    #     print(metrics_df.to_string(index=False))

    def plot_training_curves(self, plot_title=None):
            """
            Function to plot traincurves
            """
            print("Plotting training curves ...")
            FLAG = self._load_trainlogs()
            if FLAG:  
                fig, axs = plt.subplots(1, 3, figsize=(20, 6))
                plt.subplots_adjust(bottom=0.2, wspace=0.3)
                
                fig.suptitle(plot_title if plot_title is not None else self.expname, fontsize=30, fontfamily='serif', fontweight='bold')
            
                plot_traincurve(self.trainlogs, header='loss', ax=axs[0])
                plot_traincurve(self.trainlogs, header='mean_absolute_error', ax=axs[1])
                plot_traincurve(self.trainlogs, header='mean_squared_error', ax=axs[2])
            
                fig.legend(["Training", "Validation", "Min.Val."], loc='lower center', ncol=3, fontsize=16)
                
                save_fig_as = f"{self.save_path}/{self.expname}_traincurve.jpg"  
                plt.savefig(save_fig_as, format='jpg', dpi = 400, bbox_inches='tight')
