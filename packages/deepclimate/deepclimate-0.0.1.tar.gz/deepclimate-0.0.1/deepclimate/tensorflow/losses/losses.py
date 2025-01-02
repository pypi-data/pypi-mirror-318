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

def gamma_loss_mse(y_true, y_pred, thres=0.5):
    """
    Custom metric for mean squared error of gamma distribution parameters.

    Args:
        y_true (tensor): True target values.
        y_pred (tensor): Predicted values, including shape parameter, scale parameter, and occurrence probability.
        thres (float): Threshold for rainfall occurrence.

    Returns:
        tensor: The calculated mean squared error.
    """
    # Extract predicted values
    occurrence = y_pred[:, :, :, -1]
    shape_param = tf.exp(y_pred[:, :, :, 0])
    scale_param = tf.exp(y_pred[:, :, :, 1])
    
    # Calculate the rainfall using the gamma distribution
    rainfall = shape_param * scale_param * tf.cast(occurrence > thres, dtype=tf.float32)
    
    # Calculate mean squared error between predicted and true rainfall
    mse = tf.reduce_mean(tf.square(rainfall - y_true))

def gamma_loss_abs(y_true, y_pred, eps=3e-2):
    """
    Custom loss function for a gamma distribution parameterization.

    Args:
        y_true (tensor): True target values.
        y_pred (tensor): Predicted values, including shape parameter, scale parameter, and occurrence probability.
        eps (float): Small constant to prevent numerical instability.

    Returns:
        tensor: The calculated loss value.
    """
    # Extract predicted values
    y_true = y_true[:, :, :, 0]
    occurrence = y_pred[:, :, :, -1]
    shape_param = tf.exp(y_pred[:, :, :, 0])
    scale_param = tf.exp(y_pred[:, :, :, 1])
    
    # Convert y_true to a binary indicator for rain (1 if > 0.0, 0 otherwise)
    bool_rain = tf.cast(y_true > 0.0, dtype=tf.float32)
    eps = tf.constant(eps, dtype=tf.float32)
    
    # Calculate the gamma loss
    loss1 = ((1 - bool_rain) * tf.math.log(1 - occurrence + eps) +
             bool_rain * (tf.math.log(occurrence + eps) +
                          (shape_param - 1) * tf.math.log(y_true + eps) -
                          shape_param * tf.math.log(scale_param + eps) -
                          tf.math.lgamma(shape_param) -
                          y_true / (scale_param + eps)))
    
    # Calculate the absolute mean of the loss
    output_loss = tf.abs(tf.reduce_mean(loss1))
    
    return output_loss

class BernoulliGammaLoss(tf.keras.losses.Loss):
    def __init__(self, name="bernoulli_gamma_loss", reduction='sum_over_batch_size'):
        super().__init__(name=name, reduction=reduction)

    def call(self, y_true, y_pred, epsilon=1e-6):
        # Ensure epsilon is cast to the right type
        epsilon = tf.cast(epsilon, tf.float32)
        
        # Extract true values (precipitation) and predicted occurrence, shape, and scale parameters
        y_true = y_true[:,:,:,0]
        occurrence = y_pred[:,:,:,-1]
        shape_parameter = tf.exp(y_pred[:,:,:,0])
        scale_parameter = tf.exp(y_pred[:,:,:,1])

        # Boolean mask for non-zero precipitation
        bool_rain = tf.cast(y_true > 0.0, tf.float32)

        # Log-likelihood for Bernoulli-Gamma distribution
        log_likelihood = (
            (1 - bool_rain) * tf.math.log(1 - occurrence + epsilon) +
            bool_rain * (
                tf.math.log(occurrence + epsilon) +
                (shape_parameter - 1) * tf.math.log(y_true + epsilon) -
                shape_parameter * tf.math.log(scale_parameter + epsilon) -
                tf.math.lgamma(shape_parameter + epsilon) -
                y_true / (scale_parameter + epsilon)
            )
        )

        # Return the mean negative log-likelihood as the loss
        return -tf.reduce_mean(log_likelihood)

### Constrained loss function    
class ConstraintPhysicsLoss(tf.keras.losses.Loss):
    def __init__(self, reg_loss='WMAE', constraint='intensity', alpha=1, beta=1e-4, clip_min=np.log10(0.1 + 1), clip_max=np.log10(100 + 1), name="constraint_loss"):
        super().__init__(name=name)
        self.alpha = alpha
        self.beta = beta
        self.clip_min = clip_min
        self.clip_max = clip_max
        self.reg_loss = reg_loss
        self.constraint = constraint

    def __str__(self):
        return (
            f"ConstraintPhysicsLoss(reg_loss={self.reg_loss}, alpha={self.alpha}, beta={self.beta}, "
            f"clip_min={self.clip_min}, clip_max={self.clip_max}, constraint={self.constraint})"
        )
    
    def call(self, y_true, y_pred):
        # Define a dictionary mapping the regular loss options to the loss functions
        loss_dict = {
            'MSE': tf.reduce_mean(tf.square(y_true - y_pred)),
            'MAE': tf.reduce_mean(tf.abs(y_true - y_pred)),
            'WMSE': weighted_mse(y_true, y_pred, clip_min=self.clip_min, clip_max=self.clip_max),
            'WMAE': weighted_mae(y_true, y_pred, clip_min=self.clip_min, clip_max=self.clip_max),
        }
        
        # Select the regular loss function based on the reg_loss parameter
        regular_loss = loss_dict.get(self.reg_loss, None)
        if regular_loss is None:
            raise ValueError("Invalid choice of regular loss! Available options are: 'WMAE', 'MAE', 'WMSE', 'MSE'")

        # Define constraint regularization terms
        reg_dict = {
            'mass': tf.reduce_mean(tf.square(tf.reduce_sum(y_true, axis=(1, 2)) - tf.reduce_sum(y_pred, axis=(1, 2)))),
            'intensity': tf.reduce_mean(tf.square(tf.reduce_max(y_true, axis=(1, 2)) - tf.reduce_max(y_pred, axis=(1, 2)))),
        }
        
        # Select the constraint regularization term
        constraint_reg = reg_dict.get(self.constraint, None)
        if constraint_reg is None:
            raise ValueError("Invalid choice of constraint! Available options are: 'mass', 'intensity'")
    
        # Combine the regular loss and the constraint regularization term
        constraint_loss = self.alpha * regular_loss + self.beta * constraint_reg
    
        return constraint_loss

    def get_config(self):
        config = super().get_config()
        config.update({
            'alpha': self.alpha,
            'beta': self.beta,
            'clip_min': self.clip_min,
            'clip_max': self.clip_max,
            'reg_loss': self.reg_loss,
            'constraint': self.constraint,
        })
        return config

#%% Older versions of custom loss functions

def mae_loss_with_mass_conservation_(y_true, y_pred, lambda_conserv=1e-4):
    # Calculate the Mean Absolute Error (MAE)
    mae = tf.reduce_mean(tf.abs(y_true - y_pred))
    
    # Calculate the mass conservation term
    mass_conservation_error = tf.abs(tf.reduce_sum(y_true) - tf.reduce_sum(y_pred))
    
    # Combine MAE and the mass conservation term
    total_loss = mae + lambda_conserv * mass_conservation_error
    return total_loss

def gamma_loss_(y_true, y_pred, eps=3e-2):
    """
    Custom loss function for a gamma distribution parameterization.

    Args:
        y_true (tensor): True target values.
        y_pred (tensor): Predicted values, including shape parameter, scale parameter, and occurrence probability.
        eps (float): Small constant to prevent numerical instability.

    Returns:
        tensor: The calculated loss value.
    """
    # Extract true rainfall values
    y_true = y_true[:, :, :, 0]
    
    # Extract predicted occurrence, shape, and scale parameters
    occurrence = y_pred[:, :, :, -1]
    shape_param = tf.exp(y_pred[:, :, :, 0])
    scale_param = tf.exp(y_pred[:, :, :, 1])
    
    # Convert y_true to a binary indicator for rain occurrence (1 if > 0.0, 0 otherwise)
    bool_rain = tf.cast(y_true > 0.0, dtype=tf.float32)
    eps = tf.constant(eps, dtype=tf.float32)
    
    # Calculate the gamma loss
    loss1 = ((1 - bool_rain) * tf.math.log(1 - occurrence + eps) +
             bool_rain * (tf.math.log(occurrence + eps) +
                          (shape_param - 1) * tf.math.log(y_true + eps) -
                          shape_param * tf.math.log(scale_param + eps) -
                          tf.math.lgamma(shape_param) -
                          y_true / (scale_param + eps)))
    
    # Calculate the absolute mean of the loss
    output_loss = tf.abs(tf.reduce_mean(loss1))
    
    return output_loss

def gamma_loss_1d_(y_true, y_pred, eps=3e-2):
    """
    Custom loss function for a gamma distribution parameterization in 1D.

    Args:
        y_true (tensor): True target values.
        y_pred (tensor): Predicted values, including shape parameter, scale parameter, and occurrence probability.
        eps (float): Small constant to prevent numerical instability.

    Returns:
        tensor: The calculated loss value.
    """
    # Extract predicted values
    occurrence = y_pred[:, -1]
    shape_param = tf.exp(y_pred[:, 0])
    scale_param = tf.exp(y_pred[:, 1])
    
    # Convert y_true to a binary indicator for rain occurrence (1 if > 0.0, 0 otherwise)
    bool_rain = tf.cast(y_true > 0.0, dtype=tf.float32)
    eps = tf.constant(eps, dtype=tf.float32)
    
    # Calculate the gamma loss
    loss1 = ((1 - bool_rain) * tf.math.log(1 - occurrence + eps) +
             bool_rain * (tf.math.log(occurrence + eps) +
                          (shape_param - 1) * tf.math.log(y_true + eps) -
                          shape_param * tf.math.log(scale_param + eps) -
                          tf.math.lgamma(shape_param) -
                          y_true / (scale_param + eps)))
    
    # Calculate the absolute mean of the loss
    output_loss = tf.abs(tf.reduce_mean(loss1))
    
    return output_loss

#  Custom physics loss

class CustomPhysicsLoss_(tf.keras.losses.Loss):
    def __init__(self, reg_loss='WMAE', alpha=1, beta=1e-4, clip_min=np.log10(0.1 + 1), clip_max=np.log10(100 + 1), name="custom_physics_loss"):
        super().__init__(name=name)
        self.alpha = alpha
        self.beta = beta
        self.clip_min = clip_min
        self.clip_max = clip_max
        self.reg_loss = reg_loss

    def __str__(self):
        return (
            f"CustomPhysicsLoss(reg_loss={self.reg_loss}, alpha={self.alpha}, beta={self.beta}, "
            f"clip_min={self.clip_min}, clip_max={self.clip_max})"
        )
    
    def call(self, y_true, y_pred):
        # Define a dictionary mapping the regular loss options to the loss functions
        loss_dict = {
            'MSE': tf.reduce_mean(tf.square(y_true - y_pred)),
            'MAE': tf.reduce_mean(tf.abs(y_true - y_pred)),
            'WMSE': weighted_mse(y_true, y_pred, clip_min=self.clip_min, clip_max=self.clip_max),
            'WMAE': weighted_mae(y_true, y_pred, clip_min=self.clip_min, clip_max=self.clip_max),
        }
        
        # Select the regular loss function based on the reg_loss parameter
        regular_loss = loss_dict.get(self.reg_loss, None)
        
        if regular_loss is None:
            raise ValueError("Invalid choice of regular loss! Available options are 'WMAE', 'MAE', 'WMSE', and 'MSE'")
    
        # Calculate the mass conservation regularization term
        mass_conservation_error = tf.reduce_mean(tf.abs(tf.reduce_sum(y_true, axis=(1,2)) - tf.reduce_sum(y_pred, axis=(1,2))))
    
        # Combine the average difference term and the mass conservation regularization term
        custom_physics_loss = self.alpha * regular_loss + self.beta * mass_conservation_error
    
        return custom_physics_loss

    def get_config(self):
        config = super().get_config()
        config.update({
            'alpha': self.alpha,
            'beta': self.beta,
            'clip_min': self.clip_min,
            'clip_max': self.clip_max,
            'reg_loss': self.reg_loss,
        })
        return config
