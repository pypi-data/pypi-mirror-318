#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 14:41:54 2023

@author: midhunm
"""
import os
import csv
import time
import datetime as dt
import numpy as np
import pandas as pd
import tensorflow as tf
from netCDF4 import Dataset, date2num

from scipy.stats import pearsonr

def negtozero(arr):
    return np.where(arr < 0, 0, arr)

def logtrans(arr):
    return np.log10(arr + 1)

def r_logtrans(arr):
    return 10**(arr) - 1

def standardize(array):
    mean, stdv = np.nanmean(array), np.nanstd(array)
    return (array - mean)/stdv, mean, stdv

def minmaxnorm(array):
    return (array - np.nanmin(array))/(np.nanmax(array) - np.nanmin(array))

def divclip(array, c=1000):
    return np.clip((array / c), 0, 1) 

def logclip(array, c=1000, c_min=0, c_max=1):
    return np.clip(logtrans(array), c_min, c_max)

class TimeHistory(tf.keras.callbacks.Callback):
    def __init__(self, filename):
        self.filename = filename

    def on_train_begin(self, logs={}):
        self.times = []
        self.filename = self.filename

    def on_epoch_begin(self, batch, logs={}):
        self.epoch_time_start = time.time()

    def on_epoch_end(self, batch, logs={}):
        epoch_time_end = time.time()
        epoch_time = epoch_time_end - self.epoch_time_start
        self.times.append(epoch_time)
        with open(self.filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([epoch_time])
            
def load_inputs_target_pairs(inputs_channels: dict, target_channels: dict, static_channels: dict = None, data_path: str = None, as_dict=False):
    
    def check_shape_consistency(data_dict):
        shapes = [arr.shape for arr in data_dict.values()]
        if not all(shape == shapes[0] for shape in shapes):
            raise ValueError(f"Inconsistent shapes found: {shapes}")
    
    # Load input channels
    sel_inputs_channels = {}
    for channel, npy_path in inputs_channels.items():
        npy_full_path = npy_path if os.path.isabs(npy_path) else os.path.join(data_path, npy_path)
        print(f'\nLoading Inputs Channel ... {channel}: {npy_full_path}')
        sel_inputs_channels[channel] = np.load(npy_full_path)
        print(f'\tShape: {sel_inputs_channels[channel].shape}')
    
    # Check consistency and stack inputs
    check_shape_consistency(sel_inputs_channels)
    inputs = np.stack(list(sel_inputs_channels.values()), axis=3)

    print(f"\n\tFinished Processing Inputs Channels: {inputs.shape}")
    print('*'*100)
    
    # Load target channels
    sel_target_channels = {}
    for channel, npy_path in target_channels.items():
        npy_full_path = npy_path if os.path.isabs(npy_path) else os.path.join(data_path, npy_path)
        print(f'\nLoading Target Channel ... {channel}: {npy_full_path}')
        sel_target_channels[channel] = np.load(npy_full_path)
        print(f'\tShape: {sel_target_channels[channel].shape}')
    
    # Check consistency and stack targets
    check_shape_consistency(sel_target_channels)
    target = np.stack(list(sel_target_channels.values()), axis=3)

    print(f"\n\tFinished Processing Target Channels: {target.shape}")
    print('*'*100)
    
    if static_channels is not None:
        # Load static channels
        sel_static_channels = {}
        for channel, npy_path in static_channels.items():
            npy_full_path = npy_path if os.path.isabs(npy_path) else os.path.join(data_path, npy_path)
            print(f'\nLoading Static Channel ... {channel}: {npy_full_path}')
            sel_static_channels[channel] = np.load(npy_full_path)
            print(f'\tShape: {sel_static_channels[channel].shape}')
        
        # Check consistency and stack static channels
        check_shape_consistency(sel_static_channels)
        static = np.stack(list(sel_static_channels.values()), axis=3)

        print(f"\n\tFinished Processing Static Channels: {static.shape}")
        print('*'*100)
        
        result = {'inputs': inputs, 'static': static, 'target': target}
    else:
        result = {'inputs': inputs, 'target': target}
    
    return result if as_dict else tuple(result.values())

def take_paired_data_subset_by_bounds(X, y, S=None, bounds=(None, None)):
    """
    Splits data into training, validation, and test sets based on index bounds.
    Ensures that the first axis length of X and y match.
    
    Parameters:
    - X: Input features array (e.g., NumPy array, tensor, etc.)
    - y: Target array
    - S: Optional secondary input features array
    - bounds: Tuple specifying the start and end index for subsetting (inclusive, exclusive)
    
    Returns:
    - A tuple of the subsets based on the provided bounds.
    
    Raises:
    - ValueError: If the first axis of X and y are not the same length.
    """
    # Validate that the first axis lengths of X and y are the same
    if X.shape[0] != y.shape[0]:
        raise ValueError(f"The first axis lengths of X and y must match. "
                         f"Got X.shape[0] = {X.shape[0]}, y.shape[0] = {y.shape[0]}")

    # # Print the shape of data before subsetting
    # print(f"Data before subsetting:")
    # print(f"X shape: {X.shape}, y shape: {y.shape}")
    if S is not None:
        print(f"S shape: {S.shape}")

    # Subset the data
    X_subset = X[bounds[0]:bounds[1]]
    y_subset = y[bounds[0]:bounds[1]]
    S_subset = S[bounds[0]:bounds[1]] if S is not None else None

    # # Print the shape of data after subsetting
    # print(f"Data after subsetting:")
    # print(f"X_subset shape: {X_subset.shape}, y_subset shape: {y_subset.shape}")
    if S_subset is not None:
        print(f"S_subset shape: {S_subset.shape}")

    # Return the subsets
    if S is not None:
        return X_subset, S_subset, y_subset
    else:
        return X_subset, y_subset

def train_val_split_by_bounds(X, y, S=None,
                              train_bounds=(0, 9308), val_bounds=(9308, 11098), test_bounds=(11098, -1),
                              test_only=False,
                             ):
    """
    Splits data into training, validation, and test sets based on index bounds.
    """
    # Extract test data only
    if test_only:
        if S is not None:
            return (
                X[test_bounds[0]:test_bounds[1]],
                S[test_bounds[0]:test_bounds[1]],
                y[test_bounds[0]:test_bounds[1]]
            )
        else:
            return (
                X[test_bounds[0]:test_bounds[1]],
                y[test_bounds[0]:test_bounds[1]]
            )

    # Extract train and validation data
    if S is not None:
        return (
            X[train_bounds[0]:train_bounds[1]], X[val_bounds[0]:val_bounds[1]],
            S[train_bounds[0]:train_bounds[1]], S[val_bounds[0]:val_bounds[1]],
            y[train_bounds[0]:train_bounds[1]], y[val_bounds[0]:val_bounds[1]]
        )
    else:
        return (
            X[train_bounds[0]:train_bounds[1]], X[val_bounds[0]:val_bounds[1]],
            y[train_bounds[0]:train_bounds[1]], y[val_bounds[0]:val_bounds[1]]
        )

def train_val_split(X, y, S=None, train_bounds=None, val_bounds=None, test_only=False, test_bounds=12784):
    if train_bounds is None:
        train_bounds = np.concatenate([
            np.arange(366, 1827),
            np.arange(2192, 3653),
            np.arange(4018, 5479),
            np.arange(5844, 7305),
            np.arange(7671, 9132),
            np.arange(9497, 10598),
            np.arange(11322, 12784)
        ])
    
    if val_bounds is None:
        val_bounds = np.concatenate([
            np.arange(0, 366),
            np.arange(1827, 2192),
            np.arange(3653, 4018),
            np.arange(5479, 5844),
            np.arange(7305, 7671),
            np.arange(9132, 9497),
            np.arange(10598, 11322)
        ])
    
    if S is not None:
        
        if test_only:
            return X[test_bounds:], S[test_bounds:], y[test_bounds:] 
        
        else:
            return X[train_bounds], X[val_bounds], S[train_bounds], S[val_bounds], y[train_bounds], y[val_bounds]
    
    else:
        
        if test_only:
            return X[test_bounds:], y[test_bounds:] 

        else:
            return X[train_bounds], X[val_bounds], y[train_bounds], y[val_bounds]

def build_tf_data_pipeline(train_data, val_data=None, batch_size=32, train_shuffle=True):
    """
    Builds a TensorFlow data pipeline for training and optional validation datasets.
    
    Args:
        train_data: Tuple containing training data. Can be of length 2 ((x, y)) or 3 ((x1, x2), y).
        val_data: Optional tuple containing validation data. Can be of length 2 ((x, y)) or 3 ((x1, x2), y).
        batch_size: Integer, size of batches for the datasets.
    
    Returns:
        train_dataset: Preprocessed tf.data.Dataset for training.
        val_dataset: Preprocessed tf.data.Dataset for validation, or None if val_data is not provided.
    """
    
    # Create the training dataset
    if len(train_data) == 3:
        train_dataset = tf.data.Dataset.from_tensor_slices(((train_data[0], train_data[1]), train_data[2]))
    elif len(train_data) == 2:
        train_dataset = tf.data.Dataset.from_tensor_slices((train_data[0], train_data[1]))
    else:
        raise ValueError("Invalid number of training inputs.")
    
    # Shuffle, batch, and prefetch the training dataset
    if train_shuffle:
        train_dataset = train_dataset.shuffle(buffer_size=len(train_data[0]))
    train_dataset = train_dataset.batch(batch_size=batch_size)
    train_dataset = train_dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
    print("Train Dataset Element Spec:", train_dataset.element_spec)
    
    # Initialize val_dataset as None
    if val_data is None:
        return train_dataset, None
    
    # Create the validation dataset if val_data is provided
    if len(val_data) == 3:
        val_dataset = tf.data.Dataset.from_tensor_slices(((val_data[0], val_data[1]), val_data[2]))
    elif len(val_data) == 2:
        val_dataset = tf.data.Dataset.from_tensor_slices((val_data[0], val_data[1]))
    else:
        raise ValueError("Invalid number of validation inputs.")
    
    val_dataset = val_dataset.batch(batch_size=batch_size)
    val_dataset = val_dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
    print("Validation Dataset Element Spec:", val_dataset.element_spec)
    
    return train_dataset, val_dataset

def make_predictions(model, x_test, batch_size=32, isgammaloss=False, thres=0.5):
    """
    Make predictions using a trained model.

    Args:
        model (tf.keras.Model): The trained model for prediction.
        x_test (ndarray): Test data features.
        batch_size (int): Batch size for prediction.
        loss_fn (str): Type of loss function used in the model.
        thres (float): Threshold for rainfall occurrence.

    Returns:
        xarray.Dataset: A dataset containing the predicted variable.

    """
    preds = model.predict(x_test, verbose=1, batch_size=batch_size)

    if isgammaloss:
        print("\nGenerating rainfall (log) from Gamma Distribution")
        scale = np.exp(preds[:,:,:,0])
        shape = np.exp(preds[:,:,:,1])
        prob = preds[:,:,:,-1]
        rainfall = (prob > thres) * scale * shape
    else:
        print("\nGenerating rainfall (log) from WMAE")
        rainfall = preds
    return rainfall

def build_netcdf_from_array(array,
                            ref_ds=None,
                            ref_lat=None,
                            ref_lon=None,
                            varname='varname',
                            start_date="YYYY-MM-DD",
                            end_date="YYYY-MM-DD",
                            save_dir='.',
                            filename='newfile.nc',
                            delete_existing_file=True,
                            ):
    
    # Squeeze the last dimension
    array = np.squeeze(array, axis=-1)
    
    def extract_date_components(date_string):
        year, month, day = map(int, date_string.split("-"))
        return year, month, day
    
    def find_lat_lon_vars(ds):
        lat_var, lon_var = None, None
        for var_name in ds.variables:
            var = ds[var_name]
            if hasattr(var, "standard_name"):
                if var.standard_name.lower() in ["latitude", "lat"]:
                    lat_var = var_name
                elif var.standard_name.lower() in ["longitude", "lon"]:
                    lon_var = var_name
            elif var_name.lower() in ["latitude", "lat"]:
                lat_var = var_name
            elif var_name.lower() in ["longitude", "lon"]:
                lon_var = var_name
        return lat_var, lon_var
    
    def date_range(start, end):
        delta = end - start
        return [start + dt.timedelta(days=i) for i in range(delta.days + 1)]
    
    # Ensure save_dir exists
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, filename)
    
    # Remove existing file if it exists
    if delete_existing_file:
        if os.path.exists(filepath):
            os.remove(filepath)

    # Handle latitude and longitude variables
    if ref_ds is not None:
        lat_var, lon_var = find_lat_lon_vars(ref_ds)
        lat_values, lon_values = ref_ds[lat_var].data, ref_ds[lon_var].data
    elif ref_lat is not None and ref_lon is not None:
        lat_values, lon_values = ref_lat, ref_lon
    else:
        raise ValueError("Either 'ref_ds' or both 'ref_lat' and 'ref_lon' must be provided.")
    
    # Extract date components and create date range
    s_year, s_mon, s_day = extract_date_components(start_date)
    e_year, e_mon, e_day = extract_date_components(end_date)
    dates = date_range(dt.datetime(s_year, s_mon, s_day), dt.datetime(e_year, e_mon, e_day))
    
    # Validate input array shape
    expected_shape = (len(dates), len(lat_values), len(lon_values))
    if array.shape != expected_shape:
        raise ValueError(f"Input array shape {array.shape} does not match expected shape {expected_shape}.")
    
    # Create the NetCDF file
    ncfile = Dataset(filepath, mode='w', format='NETCDF4')
    ncfile.title = os.path.splitext(filename)[0]  # Add title
    
    # Create dimensions
    ncfile.createDimension('lat', len(lat_values))
    ncfile.createDimension('lon', len(lon_values))
    ncfile.createDimension('time', None)
    
    # Create variables
    lat = ncfile.createVariable('lat', np.float32, ('lat',))
    lat.units = 'degrees_north'
    lat.long_name = 'latitude'
    
    lon = ncfile.createVariable('lon', np.float32, ('lon',))
    lon.units = 'degrees_east'
    lon.long_name = 'longitude'
    
    time = ncfile.createVariable('time', np.float64, ('time',))
    time.units = f'days since {start_date}'
    time.long_name = 'time'
    
    var = ncfile.createVariable(varname, np.float64, ('time', 'lat', 'lon'))
    var.units = 'mm/day'  # Update unit appropriately
    
    # Write data
    lat[:] = lat_values
    lon[:] = lon_values
    var[:] = array
    time[:] = date2num(dates, time.units)
    
    ncfile.close()
    print(f'Dataset created: {filepath}')

def plot_traincurve(df, ax, header, label=None, ylim=None):
    ax.set_facecolor('#F0F0F0')
    ax.plot(df['epoch'], df[f'{header}'], linewidth=4, color='blue', label='Training Set')
    ax.plot(df['epoch'], df[f'val_{header}'], linewidth=2, color='red', label='Validation Set')

    min_val_loss_idx = df[f'val_{header}'].idxmin()
    min_val_loss_epoch = df.at[min_val_loss_idx, 'epoch']
    min_val_loss_value = df.at[min_val_loss_idx, f'val_{header}']

    ax.text(0.3, 0.9, f"Min.val.loss epoch: {min_val_loss_epoch}", ha='left', va='top', fontweight='normal', transform=ax.transAxes, fontsize=14)
    ax.text(0.3, 0.96, f"Min.val.loss value: {min_val_loss_value.round(4)}", ha='left', va='top', fontweight='normal', transform=ax.transAxes, fontsize=14)
    
    # ax.scatter(min_val_loss_epoch, min_val_loss_value, color='green', s=1000, marker='*', zorder=5)
    ax.axvline(x=min_val_loss_epoch, color='green', linewidth=2, linestyle='--', alpha=0.6, label='Best Model')

    ax.tick_params(axis='both', labelsize=14)
    ax.set_xlabel('EPOCHS', fontsize=16)
    ax.set_ylabel(header.upper(), fontsize=16)

    if not ylim is None:
        ax.set_ylim(ylim[0], ylim[1])

    if label is not None:
        ax.set_title(label, fontsize=18, fontweight='bold')

def fetch_inputs_target_pairs(inputs_channels: dict, target_channels: dict, static_channels: dict = None, data_path: str = None, as_dict=False):
    
    # Select Inputs Channels
    sel_inputs_channels = {}
    for channel, npy_path in inputs_channels.items():
        npy_full_path = npy_path if data_path is None else f'{data_path}/{npy_path}'
        print(f'\tLoading Inputs Channel ... {channel}: {npy_full_path}')
        sel_inputs_channels[channel] = np.load(npy_full_path).squeeze()
        print(f'\tShape: {sel_inputs_channels[channel].shape}')
    
    # Stack the input arrays
    inputs = np.stack(list(sel_inputs_channels.values()), axis=3)
    print(f"Finish Process Inputs Channels: {inputs.shape}")
    
    # Select Taget Channels
    sel_target_channels = {}
    for channel, npy_path in target_channels.items():
        npy_full_path = npy_path if data_path is None else f'{data_path}/{npy_path}'
        print(f'\tLoading Target Channel ... {channel}:  {npy_full_path}')
        sel_target_channels[channel] = np.load(npy_full_path).squeeze()
        print(f'\tShape: {sel_target_channels[channel].shape}')

    # Stack the target arrays
    target = np.stack(list(sel_target_channels.values()), axis=3)
    print(f"Finish Process Target Channels: {target.shape}")
    
    if static_channels is not None:
        # Select Static Channels
        sel_static_channels = {}
        for channel, npy_path in static_channels.items():
            npy_full_path = npy_path if data_path is None else f'{data_path}/{npy_path}'
            print(f'\tLoading Static Channel ... {channel}: {npy_full_path}')
            sel_static_channels[channel] = np.load(npy_full_path).squeeze()
            print(f'\tShape: {sel_static_channels[channel].shape}')
        
        # Stack the input arrays
        static = np.stack(list(sel_static_channels.values()), axis=3)
        print(f"Finish Process Static Channels: {static.shape}")
        
        print(f'Inputs shape: {inputs.shape} & Static shape: {static.shape} & Target shape: {target.shape}')
        
        if as_dict:
            return{
                'inputs': inputs,
                'static': static,
                'target': target,
                }
        else:
            return inputs, static, target
    
    else:
        if as_dict:
            return{
                'inputs': inputs,
                'target': target,
                }
        else:
            return inputs, target

def sel_percentile_above(data_dict, mean_series_path=None, p=25, bound=None, for_val=False):
    """ 
    Select based on percentile indices
    """
    if mean_series_path is not None:
        fsum = np.load(mean_series_path)
        if for_val:
            fsum = fsum[bound:]
        else:
            fsum = fsum[:bound]
    else:
        if bound is None:
            target = data_dict['target']
        elif for_val:
            target = data_dict['target'][bound:]
        else:
            target = data_dict['target'][:bound]
        fsum = np.nanmean(target, axis=(1, 2))

    p_thresh = np.nanpercentile(fsum, p)
    p_idx = np.where(fsum >= p_thresh)[0]

    inputs = data_dict['inputs'][p_idx]
    static = data_dict['static'][p_idx]
    target = data_dict['target'][p_idx]

    return {
        'inputs': inputs, 
        'static': static, 
        'target': target
        }

def load_data_above_percentile(
        inputs_channels: dict,
        static_channels: dict,
        target_channels: dict,
        mean_series_path: str,
        p=None, 
        bound=12419, 
        for_val=False
        ):
    """
    Data Loader for above percentile threshold
    """
    
    data_dict = fetch_inputs_target_pairs(inputs_channels, static_channels, target_channels)
    
    if p is not None:
    
        data_dict = sel_percentile_above(data_dict, mean_series_path, p, bound, for_val)
               
    return data_dict['inputs'], data_dict['static'], data_dict['target']

def interpolator(inp_arr, ups_factors):
    # input layer
    IN = x = tf.keras.layers.Input(input_size=inp_arr.shape[1:], name='unet_in')
    for _, ups_size in enumerate(ups_factors):
        x = tf.keras.layers.UpSampling2D(size=ups_size, interpolation='bilinear')(x)
    return tf.keras.models.Model(inputs=IN, outputs=x)

def compute_metrics(y_true, y_pred):
    """
    Compute evaluation metrics: MAE, MSE, RMSE, PCC, MB, and PBIAS.
    """
    # Flatten arrays to ensure consistency in shape
    y_true = y_true.flatten()
    y_pred = y_pred.flatten()
    
    # Check if the shapes of y_true and y_pred are the same
    if y_true.shape != y_pred.shape:
        raise ValueError(f"Error in compute_metrics. Shape mismatch: y_true has shape {y_true.shape}, y_pred has shape {y_pred.shape}")
    
    # Calculate the metrics
    mae = np.mean(np.abs(y_pred - y_true))  # Mean Absolute Error (MAE)
    mse = np.mean((y_pred - y_true) ** 2)   # Mean Squared Error (MSE)
    rmse = np.sqrt(mse)                     # Root Mean Squared Error (RMSE)
    pbias = np.sum(y_pred - y_true) / np.sum(y_true) * 100  # Percent Bias (PBIAS)
    mb = np.mean(y_pred - y_true)           # Mean Bias (MB)
    pcc, _ = pearsonr(y_pred, y_true)       # Pearson Correlation Coefficient
    
    # Store all metrics in a dictionary
    metrics = {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'MB': mb,
        'PCC': pcc,
        'PBIAS': pbias
    }
    
    # Convert dictionary to a pandas DataFrame for table representation and print
    metrics_df = pd.DataFrame(list(metrics.items()), columns=['Metric', 'Value'])
    return metrics_df

class CustomCSVLogger:
    def __init__(self, csv_log_path):
        self.csv_log_path = csv_log_path
        self.header_written = False  # To ensure we write the header only once

    def log_metrics(self, epoch, metrics, val_metrics=None):
        """Write logs at the end of each epoch"""
        # If the CSV file doesn't exist or the header hasn't been written, write the header
        if not os.path.exists(self.csv_log_path) or not self.header_written:
            with open(self.csv_log_path, mode='w', newline='') as f:
                writer = csv.writer(f)
                # Write the header (column names)
                writer.writerow(["epoch"] + list(metrics.keys()) + (list(val_metrics.keys()) if val_metrics else []))
                self.header_written = True

        # Append the current epoch's metrics to the file
        with open(self.csv_log_path, mode='a', newline='') as f:
            writer = csv.writer(f)
            # Combine training and validation metrics if validation metrics are provided
            row = [epoch + 1] + list(metrics.values()) + (list(val_metrics.values()) if val_metrics else [])
            writer.writerow(row)

        print(f"Epoch {epoch + 1} logs written to {self.csv_log_path}")
