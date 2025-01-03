import tensorflow as tf
import numpy as np
#%% SIMPLE_DENSE Architecture

def input_dense(x, dropout=0.5):
    """
    Apply a dense layer to the input.

    Args:
        x (tf.Tensor): Input tensor.
        dropout (float): Dropout rate.

    Returns:
        tf.Tensor: Output tensor.

    """
    flatten = tf.keras.layers.Flatten()(x)
    if dropout > 0.0:
        x = tf.keras.layers.Dropout(dropout)(flatten)
    else:
        x = flatten
    return x

def conv_layer(x, n_filters=32, activation='prelu', padding='same', kernel_size=(2, 3, 3),
              pooling=True, bn=True, strides=1):
    """
    Create a convolutional layer.
    """
    if activation=='prelu':
        x = tf.keras.layers.Conv2D(filters=n_filters, padding=padding, kernel_size=kernel_size, strides=strides)(x)
        x = tf.keras.layers.PReLU(alpha_initializer='zeros', alpha_regularizer=None, alpha_constraint=None, shared_axes=[1, 2])(x)
    else:
        x = tf.keras.layers.Conv2D(filters=n_filters, activation=activation, padding=padding, kernel_size=kernel_size, strides=strides)(x)
    if pooling:
        x = tf.keras.layers.AveragePooling2D(pool_size=(2, 2))(x)
    if bn:
        x = tf.keras.layers.BatchNormalization()(x)
    return x

def contruct_base_conv(x, layer_filters=[50, 32, 16], bn=True, padding='same', kernel_size=3, pooling=True,
                        activation='relu', dropout=0.5, strides=1):
    """
    Construct base convolutional layers for the model.
    """
    for layer_filt in layer_filters:
        x = conv_layer(x, n_filters=layer_filt, bn=bn, padding=padding, kernel_size=kernel_size, pooling=pooling,
                       activation=activation, strides=strides)
    flatten = tf.keras.layers.Flatten()(x)
    if dropout > 0.0:
        flatten = tf.keras.layers.Dropout(dropout)(flatten)
    return flatten


def LINEAR_DENSE(input_shape,
                 ups_factors, 
                 n_neurons = [256],
                 output_shape = (320,320,1),
                 dropout=0.5,
                 isgammaloss = False,
                 ):
    """
    Create a simple dense neural network model.

    Args:
        dense_layers (list): List of dense layer sizes.
        dense_activation (str): Activation function for dense layers.
        input_shape (tuple): Input shape of the model.
        dropout (float): Dropout rate.

    Returns:
        tf.keras.Model: The constructed dense neural network model.

    """
    inputs = tf.keras.layers.Input(shape=input_shape)
    x = input_dense(inputs, dropout=dropout)
    for neuron in n_neurons:
        x = tf.keras.layers.Dense(neuron)(x)
        x = tf.keras.layers.PReLU()(x)
    if isgammaloss:
        out1 = tf.keras.layers.Dense(np.prod(output_shape), activation='selu')(x)
        out1 = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(out1)
        out2 = tf.keras.layers.Dense(np.prod(output_shape), activation='selu')(x)
        out2 = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(out2)
        out3 = tf.keras.layers.Dense(np.prod(output_shape), activation='sigmoid')(x)
        out3 = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(out3)
        out = tf.keras.layers.Concatenate()([out1, out2, out3])
        return tf.keras.models.Model(inputs, out, name='LINEAR-DENSE-x3')
    else:  
        x = tf.keras.layers.Dense(np.prod(output_shape))(x)
        x = tf.keras.layers.PReLU()(x)
        x = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(x)
        return tf.keras.models.Model(inputs, x, name='LINEAR-DENSE')


#%% CONV_DENSE Architecture

def CONV_DENSE(input_shape,
                ups_factors,
                layer_filters=[16, 64, 128], 
                bn=True, 
                padding='same', 
                kernel_size=3,
                pooling=True, 
                dense_layers=[256], 
                dense_activation=tf.keras.layers.PReLU(),
                dropout=0.5, 
                activation=tf.keras.layers.PReLU(),
                isgammaloss = False,
                ):
    """
    Create a complex convolutional neural network model.
    """
    inputs = tf.keras.layers.Input(shape=input_shape)
    x = contruct_base_conv(inputs, layer_filters=layer_filters, bn=bn, padding=padding,
                         kernel_size=kernel_size, pooling=pooling, activation=activation, dropout=dropout)
    for neuron in dense_layers:
        if activation=='prelu':
            x = tf.keras.layers.Dense(neuron)(x)
            x = tf.keras.layers.PReLU()(x)
        else:
            x = tf.keras.layers.Dense(neuron, activation=activation)(x)
        # x = tf.keras.layers.Dropout(dropout)(x)
    if isgammaloss:
        out1 = tf.keras.layers.Dense(np.prod(ups_factors)*input_shape[0]*np.prod(ups_factors)*input_shape[1], 
                                     activation='selu', kernel_initializer='zeros')(x)
        out1 = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(out1)
        out2 = tf.keras.layers.Dense(np.prod(ups_factors)*input_shape[0]*np.prod(ups_factors)*input_shape[1], 
                                     activation='selu', kernel_initializer='zeros')(x)
        out2 = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(out2)
        out3 = tf.keras.layers.Dense(np.prod(ups_factors)*input_shape[0]*np.prod(ups_factors)*input_shape[1], 
                                     activation='sigmoid', kernel_initializer='zeros')(x)
        out3 = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(out3)
        out = tf.keras.layers.Concatenate()([out1, out2, out3])
        return tf.keras.models.Model(inputs, out, name='CONV-DENSE-x3')
    else:
        x = tf.keras.layers.Dense(np.prod(ups_factors)*input_shape[0]*np.prod(ups_factors)*input_shape[1], 
                                  activation='linear', kernel_initializer='zeros')(x)
        x = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(x)
        return tf.keras.models.Model(inputs, x, name='CONV-DENSE')


#%% FSRCNN Architecture

def FSRCNN(input_shape,
           ups_factors,
           k_size = 3, 
           n = 128,
           d = 64, 
           s = 32,
           m = 4, 
           isgammaloss = False,
           ):
    """
    FSRCNN model implementation from https://arxiv.org/abs/1608.00367
    
    Sigmoid Activation in the output layer is not in the original paper.
    But it is needed to align model prediction with ground truth HR images
    so their values are in the same range [0,1].
    """
    
    inputs = tf.keras.layers.Input(shape = input_shape)
    # feature extraction
    model = tf.keras.layers.Conv2D(kernel_size=5, filters=d, padding="same", kernel_initializer=tf.keras.initializers.HeNormal())(inputs)
    model = tf.keras.layers.PReLU(alpha_initializer="zeros", shared_axes=[1, 2])(model)
    # Shrinking
    model = tf.keras.layers.Conv2D(kernel_size=1, filters=s, padding="same", kernel_initializer=tf.keras.initializers.HeNormal())(model)
    model = tf.keras.layers.PReLU(alpha_initializer="zeros", shared_axes=[1, 2])(model)
    # Mapping
    for _ in range(m):
        model = tf.keras.layers.Conv2D(kernel_size=3, filters=s, padding="same", kernel_initializer=tf.keras.initializers.HeNormal())(model)
        model = tf.keras.layers.PReLU(alpha_initializer="zeros", shared_axes=[1, 2])(model)
    # Expanding
    model = tf.keras.layers.Conv2D(kernel_size=1, filters=d, padding="same")(model)
    model = tf.keras.layers.PReLU(alpha_initializer="zeros", shared_axes=[1, 2])(model)
    # Deconvolution
    for _, ups_size in enumerate(ups_factors):
        model =tf.keras.layers.Conv2DTranspose(kernel_size=3, filters=n, strides=ups_size, padding="same", 
                                             kernel_initializer=tf.keras.initializers.RandomNormal(mean=0, stddev=0.001))(model)
        model = tf.keras.layers.PReLU(alpha_initializer="zeros", shared_axes=[1, 2])(model)
    if isgammaloss:
        out1 = tf.keras.layers.Conv2D(kernel_size=k_size, filters=1, padding="same", 
                                   activation='selu', kernel_initializer=tf.keras.initializers.HeNormal())(model)
        out2 = tf.keras.layers.Conv2D(kernel_size=k_size, filters=1, padding="same", 
                                   activation='selu', kernel_initializer=tf.keras.initializers.HeNormal())(model)
        out3 = tf.keras.layers.Conv2D(kernel_size=k_size, filters=1, padding="same", 
                                   activation='sigmoid', kernel_initializer=tf.keras.initializers.HeNormal())(model)
        out = tf.keras.layers.Concatenate()([out1, out2, out3])
        return tf.keras.models.Model(inputs, out, name='FSRCNN-x3')
    else:
        model = tf.keras.layers.Conv2D(kernel_size=k_size, filters=1, padding="same", 
                                       kernel_initializer=tf.keras.initializers.HeNormal())(model)
        return tf.keras.models.Model(inputs, model, name='FSRCNN')