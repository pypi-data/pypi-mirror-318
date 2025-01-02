import numpy as np
import pandas as pd
import scipy as sc 

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
    pcc, _ = sc.stats.pearsonr(y_pred, y_true)       # Pearson Correlation Coefficient
    
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