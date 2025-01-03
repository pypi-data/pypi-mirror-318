import numpy as np
import tensorflow as tf

# SRDRN Activation block
def SRDRN_activation(model, activation='prelu'):    
    """
    Apply activation function to the given model.
    """
    
    if activation == 'relu':
        return tf.keras.layers.ReLU()(model)
    elif activation == 'leaky':
        return tf.keras.layers.LeakyReLU(alpha=0.3)(model)
    elif activation == 'prelu':    
        return tf.keras.layers.PReLU(alpha_initializer='zeros', alpha_regularizer=None, alpha_constraint=None, shared_axes=[1, 2])(model)
    else:
        return model  # Return the input model if no activation is specified

# SRDRN Residual block
def SRDRN_residual_block(model, kernal_size, n_filters, strides, regularizer, initializer, activation):
    """
    Constructs a residual block for the Super-resolution Residual Deep Neural Network (SRDRN).
    """
    gen = model    
    model = tf.keras.layers.Conv2D(filters = n_filters, kernel_size = kernal_size, strides = strides, padding = "same", kernel_regularizer=regularizer, kernel_initializer=initializer)(model)
    model = tf.keras.layers.BatchNormalization(momentum = 0.5)(model)
    model = SRDRN_activation(model, activation=activation)
    model = tf.keras.layers.Conv2D(filters = n_filters, kernel_size = kernal_size, strides = strides, padding = "same", kernel_regularizer=regularizer, kernel_initializer=initializer)(model)
    model = tf.keras.layers.BatchNormalization(momentum = 0.5)(model)    
    model = tf.keras.layers.add([gen, model])    
    return model

# SRDRN Upsampling block
def SRDRN_upsampling_block(model, ups_size, n_filters, activation, regularizer, initializer, interpolation):
    """
    Constructs an upsampling block for the Super-resolution Residual Deep Neural Network (SRDRN).
    """
    model = tf.keras.layers.Conv2D(filters = n_filters, kernel_size = 3, strides = 1, padding = "same", kernel_regularizer=regularizer, kernel_initializer=initializer)(model)
    model = tf.keras.layers.UpSampling2D(size = ups_size, interpolation = interpolation)(model)
    model = SRDRN_activation(model, activation=activation)
    # print('*'*20, str(interpolation), '*'*20)
    return model

def SRDRN_convtranspose_block(model, ups_size, n_filters, activation, regularizer, initializer):
    """
    Constructs an upsampling block for the Super-resolution Residual Deep Neural Network (SRDRN).
    """
    model = tf.keras.layers.Conv2DTranspose(filters=n_filters, kernel_size=3, strides=ups_size, padding="same",
                                         kernel_regularizer=regularizer, kernel_initializer=initializer)(model)
    model = SRDRN_activation(model, activation=activation)
    return model

### Build Architectures ###

def SRDRN(input_shape,
          ups_factors,
          n_filters = 64,
          n_res_blocks = 16, 
          n_ups_filters = 256,
          n_classes = 3,
          activation = 'prelu',
          regularizer = tf.keras.regularizers.l2(0.01),
          initializer = tf.keras.initializers.RandomNormal(stddev=0.02), 
          interpolation='nearest',
          isgammaloss = False,
          ):
    
    """
    Constructs a Super-resolution Residual Deep Neural Network (SRDRN) generator model (Wang et al. 2020).
    """
    
    inputs = tf.keras.layers.Input(shape = input_shape)
    model = tf.keras.layers.Conv2D(filters = n_filters, kernel_size = 3, strides = 1, padding = "same", 
                                kernel_regularizer=regularizer, kernel_initializer=initializer)(inputs)
    model = SRDRN_activation(model, activation=activation)
    gen_model = model
    # Using 16 Residual Blocks
    for _ in range(n_res_blocks):
        model = SRDRN_residual_block(model, kernal_size=3, n_filters=n_filters, strides=1, 
                                     regularizer=regularizer, initializer=initializer, activation=activation)
    model = tf.keras.layers.Conv2D(filters = n_filters, kernel_size = 3, strides = 1, padding = "same", 
                                kernel_initializer=initializer)(model)
    model = tf.keras.layers.BatchNormalization(momentum = 0.5)(model)
    model = tf.keras.layers.add([gen_model, model])
    for _, ups_size in enumerate(ups_factors):
        model = SRDRN_upsampling_block(model, ups_size=ups_size, n_filters=n_ups_filters, 
                                       activation=activation, regularizer=regularizer, initializer=initializer, 
                                       interpolation=interpolation)  
    if isgammaloss:
        out1 = tf.keras.layers.Conv2D(filters = 1, kernel_size = n_classes, strides = 1, activation='selu', 
                                  padding = "same", kernel_regularizer=regularizer, 
                                  kernel_initializer=initializer)(model)
        out2 = tf.keras.layers.Conv2D(filters = 1, kernel_size = n_classes, strides = 1, activation='selu', 
                                  padding = "same", kernel_regularizer=regularizer, 
                                  kernel_initializer=initializer)(model)
        out3 = tf.keras.layers.Conv2D(filters = 1, kernel_size = n_classes, strides = 1, activation='sigmoid', 
                                  padding = "same", kernel_regularizer=regularizer, 
                                  kernel_initializer=initializer)(model)
        out = tf.keras.layers.Concatenate()([out1, out2, out3])
        return tf.keras.models.Model(inputs, out, name='SRDRN-x3')
    else:
        model = tf.keras.layers.Conv2D(filters = 1, kernel_size = n_classes, strides = 1, activation='linear', 
                                  padding = "same", kernel_regularizer=regularizer, 
                                  kernel_initializer=initializer)(model)
        return tf.keras.models.Model(inputs, model, name='SRDRN')

#%% s02: SRDRN_TC Architecture

def SRDRN_TC(input_shape,
             ups_factors,
             n_filters = 64,
             n_res_blocks = 16, 
             n_ups_filters = 256,
             n_classes = 1, 
             activation = 'prelu',
             regularizer = tf.keras.regularizers.l2(0.01),
             initializer = tf.keras.initializers.RandomNormal(stddev=0.02),
             isgammaloss = False,
             ):
    
    """
    Constructs a Super-resolution Residual Deep Neural Network (SRDRN) generator model (Wang et al. 2020).
    """
    
    inputs = tf.keras.layers.Input(shape = input_shape)
    model = tf.keras.layers.Conv2D(filters = n_filters, kernel_size = 3, strides = 1, padding = "same", 
                                kernel_regularizer=regularizer, kernel_initializer=initializer)(inputs)
    model = SRDRN_activation(model, activation=activation)
    gen_model = model
    # Using 16 Residual Blocks
    for _ in range(n_res_blocks):
        model = SRDRN_residual_block(model, kernal_size=3, n_filters=n_filters, strides=1, 
                                     regularizer=regularizer, initializer=initializer, activation=activation)
    model = tf.keras.layers.Conv2D(filters = n_filters, kernel_size = 3, strides = 1, padding = "same", 
                                kernel_initializer=initializer)(model)
    model = tf.keras.layers.BatchNormalization(momentum = 0.5)(model)
    model = tf.keras.layers.add([gen_model, model])
    for _, ups_size in enumerate(ups_factors):
        model = SRDRN_convtranspose_block(model, ups_size=ups_size, n_filters=n_ups_filters, 
                                          activation=activation, regularizer=regularizer, 
                                          initializer=initializer)  
    if isgammaloss:
        out1 = tf.keras.layers.Conv2D(filters = 1, kernel_size = n_classes, strides = 1, activation='selu', 
                                  padding = "same", kernel_regularizer=regularizer, 
                                  kernel_initializer=initializer)(model)
        out2 = tf.keras.layers.Conv2D(filters = 1, kernel_size = n_classes, strides = 1, activation='selu', 
                                  padding = "same", kernel_regularizer=regularizer, 
                                  kernel_initializer=initializer)(model)
        out3 = tf.keras.layers.Conv2D(filters = 1, kernel_size = n_classes, strides = 1, activation='sigmoid', 
                                  padding = "same", kernel_regularizer=regularizer, 
                                  kernel_initializer=initializer)(model)
        out = tf.keras.layers.Concatenate()([out1, out2, out3])
        return tf.keras.models.Model(inputs, out, name='SRDRN-TC-x3')
    else:
        model = tf.keras.layers.Conv2D(filters = 1, kernel_size = n_classes, strides = 1, activation='linear', 
                                  padding = "same", kernel_regularizer=regularizer, 
                                  kernel_initializer=initializer)(model)
        return tf.keras.models.Model(inputs, model, name='SRDRN-TC')


#%% s03: SRDRN_DENSE Architecture

def SRDRN_DENSE(input_shape,
                ups_factors,
                n_filters = 64,
                n_res_blocks = 16, 
                n_ups_filters = 256,
                n_dense=256,
                dropout = 0.5,
                activation = 'prelu',
                regularizer = tf.keras.regularizers.l2(0.01),
                initializer = tf.keras.initializers.RandomNormal(stddev=0.02), 
                isgammaloss = False,
                ):
    
    """
    Constructs a Super-resolution Residual Deep Neural Network (SRDRN) generator model (Wang et al. 2020).
    """
    
    inputs = tf.keras.layers.Input(shape = input_shape)
    model = tf.keras.layers.Conv2D(filters = n_filters, kernel_size = 3, strides = 1, padding = "same", 
                                kernel_regularizer=regularizer, kernel_initializer=initializer)(inputs)
    model = SRDRN_activation(model, activation=activation)
 
    gen_model = model
    
    # Using 16 Residual Blocks
    for _ in range(n_res_blocks):
        model = SRDRN_residual_block(model, kernal_size=3, n_filters=n_filters, strides=1, 
                                     regularizer=regularizer, initializer=initializer, activation=activation)
    
    model = tf.keras.layers.Conv2D(filters = n_filters, kernel_size = 3, strides = 1, padding = "same", 
                                kernel_initializer=initializer)(model)
    model = tf.keras.layers.BatchNormalization(momentum = 0.5)(model)
    model = tf.keras.layers.add([gen_model, model])
    
    model = tf.keras.layers.Conv2D(filters = 1, kernel_size = 3, strides = 1, padding = "same",
                            kernel_regularizer=regularizer, kernel_initializer=initializer)(model)
    model = SRDRN_activation(model, activation=activation)
    
    # Initiate Dense layers
    model = tf.keras.layers.Flatten()(model)
    model = tf.keras.layers.Dense(n_dense)(model)
    model = tf.keras.layers.PReLU()(model)
    model = tf.keras.layers.Dropout(dropout)(model)
    
    if isgammaloss:
        out1 = tf.keras.layers.Dense(np.prod(ups_factors)*input_shape[0]*np.prod(ups_factors)*input_shape[1], 
                                     activation='selu', kernel_initializer='zeros')(model)
        out1 = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(out1)
        out2 = tf.keras.layers.Dense(np.prod(ups_factors)*input_shape[0]*np.prod(ups_factors)*input_shape[1], 
                                     activation='selu', kernel_initializer='zeros')(model)
        out2 = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(out2)
        out3 = tf.keras.layers.Dense(np.prod(ups_factors)*input_shape[0]*np.prod(ups_factors)*input_shape[1], 
                                     activation='sigmoid', kernel_initializer='zeros')(model)
        out3 = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(out3)
        out = tf.keras.layers.Concatenate()([out1, out2, out3])
        return tf.keras.models.Model(inputs, out, name='SRDRN-DENSE-x3')
    else:
        model = tf.keras.layers.Dense(np.prod(ups_factors)*input_shape[0]*np.prod(ups_factors)*input_shape[1], kernel_initializer='zeros')(model)
        model = tf.keras.layers.Activation("linear")(model)
        out = tf.keras.layers.Reshape((np.prod(ups_factors)*input_shape[0],np.prod(ups_factors)*input_shape[1],1))(model)
        return tf.keras.models.Model(inputs, out, name='SRDRN-DENSE')
