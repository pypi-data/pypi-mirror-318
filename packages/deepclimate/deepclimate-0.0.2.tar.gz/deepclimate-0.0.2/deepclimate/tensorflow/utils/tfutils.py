import csv
import time
import numpy as np
import tensorflow as tf

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

def interpolator(inp_arr, ups_factors):
    # input layer
    IN = x = tf.keras.layers.Input(input_size=inp_arr.shape[1:], name='unet_in')
    for _, ups_size in enumerate(ups_factors):
        x = tf.keras.layers.UpSampling2D(size=ups_size, interpolation='bilinear')(x)
    return tf.keras.models.Model(inputs=IN, outputs=x)

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