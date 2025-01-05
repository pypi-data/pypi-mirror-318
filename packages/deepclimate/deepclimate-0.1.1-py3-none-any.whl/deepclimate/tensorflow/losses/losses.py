#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 12:15:55 2024

@author: midhunm
"""
import numpy as np
import tensorflow as tf

#%% Implementation of Custom loss functions

def weighted_mae(
        y_true, y_pred, 
        clip_min=tf.math.log(tf.constant(0.1 + 1, dtype=tf.float32)), 
        clip_max=tf.math.log(tf.constant(100 + 1, dtype=tf.float32))
        ):
    """
    Weighted mean absolute error (MAE) loss function.
    Weights are calculated based on the true values, with higher weights assigned to larger values.
    """
    weights = tf.clip_by_value(y_true, clip_min, clip_max)
    loss = tf.reduce_mean(tf.multiply(weights, tf.abs(y_true - y_pred)))
    return loss

def weighted_mse(
        y_true, y_pred, 
        clip_min=tf.math.log(tf.constant(0.1 + 1, dtype=tf.float32)), 
        clip_max=tf.math.log(tf.constant(100 + 1, dtype=tf.float32))
        ):
    """
    Weighted mean squared error (MSE) loss function.
    Weights are calculated based on the true values, with higher weights assigned to larger values.
    """
    # Calculate the weights for each data point
    weights = tf.clip_by_value(y_true, clip_min, clip_max)
    # Calculate the weighted mean squared error
    loss = tf.reduce_mean(tf.multiply(weights, tf.square(y_true - y_pred)))
    return loss