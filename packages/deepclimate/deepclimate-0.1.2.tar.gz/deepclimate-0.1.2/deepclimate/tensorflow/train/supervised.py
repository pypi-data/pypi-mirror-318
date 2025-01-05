#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 01:50:28 2024

@author: midhunmachari@gmail.com
"""

# Import libraries
import os
import sys
import time
import datetime
import warnings
import numpy as np
import pandas as pd
import xarray as xr
import tensorflow as tf
from ..utils import build_tf_data_pipeline

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
