#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:22:40 2023

@author: midhunmachari@gmail.com
"""
#%% Network Construct Utilities
import numpy as np
import tensorflow as tf

def stride_conv(X, channel, pool_size=2, activation='relu', 
                initializer=tf.keras.initializers.RandomNormal(stddev=0.02),
                regularizer=tf.keras.regularizers.l2(0.01),
                name='X'):
    '''
    stride convolutional layer --> batch normalization --> Activation
    *Proposed to replace max- and average-pooling layers

    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        pool_size: size of stride
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU
        name: name of created keras layers

    Output               regularizer = keras.regularizers.l2(0.01),
              initializer = 
    ----------
        X: output tensor
    '''
    # linear convolution with strides
    X = tf.keras.layers.Conv2D(channel, pool_size, strides=(pool_size, pool_size), padding='valid', use_bias=False, 
                               kernel_initializer=initializer, kernel_regularizer=regularizer,
                               kernet_name=f'{name}_stride_conv')(X)
    # batch normalization
    X = tf.keras.layers.BatchNormalization(axis=3, name=f'{name}_stride_conv_bn')(X)

    # activation
    if activation == 'relu':
        X = tf.keras.layers.ReLU(name=f'{name}_stride_conv_relu')(X)
    elif activation == 'leaky':
        X = tf.keras.layers.LeakyReLU(negative_slope=0.3, name=f'{name}_stride_conv_leaky')(X)
    elif activation == 'prelu':
            X = tf.keras.layers.PReLU(alpha_initializer='zeros', alpha_regularizer=None, alpha_constraint=None, 
                                      shared_axes=[1, 2], name=f'{name}_stride_conv_prelu')(X)

    return X

def CONV_stack(X, channel, kernel_size=3, stack_num=2, 
               initializer=tf.keras.initializers.RandomNormal(stddev=0.02),
               regularizer=tf.keras.regularizers.l2(0.01),
               activation='relu', name='conv_stack'):
    '''
    (Convolutional layer --> batch normalization --> Activation)*stack_num

    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        stack_num: number of stacked convolutional layers
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU
        name: name of created keras layers

    Output
    ----------
        X: output tensor

    '''

    # stacking Convolutional layers
    for i in range(stack_num):

        # linear convolution
        X = tf.keras.layers.Conv2D(channel, kernel_size, padding='same', use_bias=False,
                                kernel_initializer=initializer, kernel_regularizer=regularizer, 
                                name=f'{name}_stack{i}_conv')(X)

        # batch normalization
        X = tf.keras.layers.BatchNormalization(axis=3, name=f'{name}_stack{i}_bn')(X)

        # activation
        if activation == 'relu':
            X = tf.keras.layers.ReLU(name=f'{name}_stack{i}_relu')(X)
        elif activation == 'leaky':
            X = tf.keras.layers.LeakyReLU(negative_slope=0.3, name=f'{name}_stack{i}_leaky')(X)
        elif activation == 'prelu':
            X = tf.keras.layers.PReLU(alpha_initializer='zeros', alpha_regularizer=None, alpha_constraint=None, 
                                      shared_axes=[1, 2], name=f'{name}_stack{i}_prelu')(X)

    return X


def EncoderBlock(X, channel, kernel_size=3, pool_size=2, pool=True, dropout_rate=0, activation='relu', name='left0'): # UNET_left
    '''
    Encoder block of UNet

    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        pool_size: size of stride
        pool: True for maxpooling, False for strided convolutional layers
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU
        name: name of created keras layers

    Output
    ----------
        X: output tensor

    '''

    # maxpooling layer vs strided convolutional layers
    if pool:
        X = tf.keras.layers.MaxPooling2D(pool_size=(pool_size, pool_size), name=f'{name}_pool')(X)
    else:
        X = stride_conv(X, channel, pool_size, activation=activation, name=name)

    # stack linear convolutional layers
    X = CONV_stack(X, channel, kernel_size, stack_num=1, activation=activation, name=name)
    
    # Apply dropout after convolutional stack
    if dropout_rate > 0:
        X = tf.keras.layers.Dropout(dropout_rate, name=f'{name}_dropout')(X)

    return X

def DecoderBlock(X, X_left, channel, kernel_size=3, pool_size=2, dropout_rate=0, activation='relu', name='right0'): # UNET_right
    '''
    Decoder block of UNet

    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        pool_size: size of transpose stride, expected to be the same as "UNET_left"
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU
        name: name of created keras layers

    Output
    ----------
        X: output tensor

    '''

    # Transpose convolutional layer --> stacked linear convolutional layers
    X = tf.keras.layers.Conv2DTranspose(channel, kernel_size, strides=(pool_size, pool_size),
                                     padding='same', name=f'{name}_trans_conv')(X)
    X = CONV_stack(X, channel, kernel_size, stack_num=1, activation=activation, name=f'{name}_conv_after_trans')

    # Tensor concatenation
    H = tf.keras.layers.concatenate([X_left, X], axis=3)

    # stacked linear convolutional layers after concatenation
    H = CONV_stack(H, channel, kernel_size, stack_num=1, activation=activation, name=f'{name}_conv_after_concat')

    # Apply dropout after concatenation and final convolution
    if dropout_rate > 0:
        H = tf.keras.layers.Dropout(dropout_rate, name=f'{name}_dropout')(H)

    return H

def attention_gate(x, g, inter_channels, name='attention'):
    """
    Attention Gate module to focus on relevant features in skip connections.

    Input
    ----------
        x: Tensor from the encoder (skip connection).
        g: Tensor from the decoder (guidance signal).
        inter_channels: Number of intermediate channels.
        name: Name for the layers.

    Output
    ----------
        out: Attention-weighted tensor.
    """
    # 1x1 convolution for input x
    theta_x = tf.keras.layers.Conv2D(inter_channels, kernel_size=1, strides=1, padding='same', name=f'{name}_theta_x')(x)
    
    # 1x1 convolution for input g
    phi_g = tf.keras.layers.Conv2D(inter_channels, kernel_size=1, strides=1, padding='same', name=f'{name}_phi_g')(g)
    
    # Add x and g, followed by ReLU
    f = tf.keras.layers.Activation('relu', name=f'{name}_relu')(theta_x + phi_g)
    
    # 1x1 convolution to get attention coefficients
    psi = tf.keras.layers.Conv2D(1, kernel_size=1, strides=1, padding='same', name=f'{name}_psi')(f)
    psi = tf.keras.layers.Activation('sigmoid', name=f'{name}_sigmoid')(psi)
    
    # print(f"x shape: {str(x.shape):<20} psi shape: {psi.shape}")
    
    # Multiply input x by attention coefficients
    out = tf.keras.layers.Multiply(name=f'{name}_multiply')([x, psi])
    
    return out

def DecoderBlock_with_attention(X, X_left, channel, inter_channel=None, kernel_size=3, 
                              pool_size=2, dropout_rate=0, activation='relu', name='right0'): # UNET_right_with_attention
    """
    Decoder block of Attention U-Net.
    """
    # Transpose convolutional layer --> stacked linear convolutional layers
    X = tf.keras.layers.Conv2DTranspose(channel, kernel_size, strides=(pool_size, pool_size),
                                         padding='same', name=f'{name}_trans_conv')(X)
    X = CONV_stack(X, channel, kernel_size, stack_num=1, activation=activation, name=f'{name}_conv_after_trans')

    # Apply Attention Gate to the skip connection
    X_left_att = attention_gate(X_left, X, inter_channels = channel // inter_channel if inter_channel is not None else channel, 
                                name=f'{name}_attention_gate')

    # Tensor concatenation
    H = tf.keras.layers.concatenate([X_left_att, X], axis=3)

    # Stacked linear convolutional layers after concatenation
    H = CONV_stack(H, channel, kernel_size, stack_num=1, activation=activation, name=f'{name}_conv_after_concat')
    
    # Apply dropout after concatenation and final convolution
    if dropout_rate > 0:
        H = tf.keras.layers.Dropout(dropout_rate, name=f'{name}_dropout')(H)

    return H

#%% u01: UNET

def UNET(
        input_shape, 
        layer_N=[64, 96, 128, 160],
        input_stack_num=2, 
        pool=True, 
        activation='relu',
        n_classes = 1,
        dropout_rate=0.3,
        isgammaloss=False,
        ):
    '''
    UNet with three down- and upsampling levels.
    '''
    
    IN_LR = tf.keras.layers.Input(input_shape) # unet_in_lr
    
    x01 = IN_LR
    
    # Encoder  
    X_en1 = CONV_stack(x01, layer_N[0], kernel_size=3, stack_num=input_stack_num, activation=activation, name='unet_left0') 
    X_en2 = EncoderBlock(X_en1, layer_N[1], pool=pool, activation=activation, name='unet_left1')
    X_en3 = EncoderBlock(X_en2, layer_N[2], pool=pool, activation=activation, name='unet_left2')
    
    # Bottleneck
    X4 = EncoderBlock(X_en3, layer_N[3], pool=pool, activation=activation, name='unet_bottom')
    
    # Decoder
    X_de3 = DecoderBlock(X4, X_en3, layer_N[2], activation=activation, dropout_rate=dropout_rate, name='unet_right2')
    X_de2 = DecoderBlock(X_de3, X_en2, layer_N[1], activation=activation, dropout_rate=dropout_rate, name='unet_right1')
    X_de1 = DecoderBlock(X_de2, X_en1, layer_N[0], activation=activation, dropout_rate=dropout_rate, name='unet_right0')
    # output
    x = CONV_stack(X_de1, 16, kernel_size=3, stack_num=1, activation=activation, name='unet_out')
    
    if isgammaloss:
        out1 = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                      activation='selu', padding='same', name='unet_out1')(x)
        out2 = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                      activation='selu', padding='same', name='unet_out2')(x)
        out3 = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                      activation='sigmoid', padding='same', name='unet_out3')(x)
        OUT = tf.keras.layers.Concatenate()([out1, out2, out3])
        return tf.keras.models.Model(inputs=IN_LR, outputs=OUT, name='UNET-GAMMA')
    else:
        OUT = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                     activation="linear", padding='same', name='unet_out')(x)
        return tf.keras.models.Model(inputs=IN_LR, outputs=OUT, name='UNET')

# if __name__ == "__main__":

#     u1 = UNET(
#         input_shape=(160,360,7), 
#         layer_N=[64, 96, 128, 160],
#         input_stack_num=2, 
#         pool=True, 
#         activation='prelu',
#         n_classes = 1,
#         dropout_rate=0.25,
#         isgammaloss=False,
#         )
#     u1.summary()

#%% Attention UNet

def Attention_UNET(
        input_shape, 
        layer_N=[64, 96, 128, 160],
        input_stack_num=2, 
        pool=True, 
        activation='prelu',
        n_classes=1,
        dropout_rate=0.3,
        isgammaloss=False,
        ):
    """
    Attention U-Net with three down- and upsampling levels.
    """
    IN_LR = tf.keras.layers.Input(input_shape)

    x01 = IN_LR

    # Encoder
    X_en1 = CONV_stack(x01, layer_N[0], kernel_size=3, stack_num=input_stack_num, activation=activation, name='unet_left0') 
    X_en2 = EncoderBlock(X_en1, layer_N[1], pool=pool, activation=activation, name='unet_left1')
    X_en3 = EncoderBlock(X_en2, layer_N[2], pool=pool, activation=activation, name='unet_left2')
    
    # Bottleneck
    X4 = EncoderBlock(X_en3, layer_N[3], pool=pool, activation=activation, name='unet_bottom')

    # Decoder (upsampling with Attention)
    X_de3 = DecoderBlock_with_attention(X4, X_en3, layer_N[2], inter_channel=None, activation=activation, dropout_rate=dropout_rate, name='unet_right2')
    X_de2 = DecoderBlock_with_attention(X_de3, X_en2, layer_N[1], inter_channel=2, activation=activation, dropout_rate=dropout_rate, name='unet_right1')
    X_de1 = DecoderBlock_with_attention(X_de2, X_en1, layer_N[0], inter_channel=2, activation=activation, dropout_rate=dropout_rate, name='unet_right0')

    # Output
    x = CONV_stack(X_de1, 16, kernel_size=3, stack_num=1, activation=activation, name='unet_out')
    if isgammaloss:
        out1 = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                      activation='selu', padding='same', name='unet_out1')(x)
        out2 = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                      activation='selu', padding='same', name='unet_out2')(x)
        out3 = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                      activation='sigmoid', padding='same', name='unet_out3')(x)
        OUT = tf.keras.layers.Concatenate()([out1, out2, out3])
        return tf.keras.models.Model(inputs=[IN_LR], outputs=[OUT], name='ATTENTION-UNET-GAMMA')
    else:
        OUT = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                     activation="linear", padding='same', name='unet_out')(x)
        return tf.keras.models.Model(inputs=IN_LR, outputs=OUT, name='ATTENTION-UNET')

# if __name__ == "__main__":
    
#     u2 = Attention_UNET(
#         input_shape=(160,360,7), 
#         layer_N=[64, 96, 128, 160],
#         input_stack_num=2, 
#         pool=True, 
#         activation='prelu',
#         n_classes=1,
#         dropout_rate=0.25,
#         isgammaloss=False
#         )
#     u2.summary()
    
#%% Discriminator Architecture

def Discriminator(
        inputs_shape, 
        layer_N=[64, 96, 128, 160],
        input_stack_num=2, 
        pool=True, 
        activation='leaky',
        initializer = tf.random_normal_initializer(0., 0.02)
        ):
    
    INP = tf.keras.layers.Input(shape=inputs_shape, name='input_image')
    
    x01 = INP
    
    # Encoder
    X_en1 = CONV_stack(x01, layer_N[0], kernel_size=3, stack_num=input_stack_num, activation=activation, name='disc_left0') 
    X_en2 = EncoderBlock(X_en1, layer_N[1], pool=pool, activation=activation, name='disc_left1')
    X_en3 = EncoderBlock(X_en2, layer_N[2], pool=pool, activation=activation, name='disc_left2')
    
    # Bottleneck
    X4 = EncoderBlock(X_en3, layer_N[3], pool=pool, activation=activation, name='disc_bottom')
    
    # Final output
    x00 = tf.keras.layers.BatchNormalization()(X4)
    x00 = tf.keras.layers.LeakyReLU()(x00)
    x00 = tf.keras.layers.Conv2D(1, 4, strides=1, kernel_initializer=initializer)(x00)
    x00 = tf.keras.layers.Flatten()(x00)
    x00 = tf.keras.layers.Dense(128)(x00)
    x00 = tf.keras.layers.Activation('relu')(x00)
    x00 = tf.keras.layers.Dropout(0.5)(x00) 
    x00 = tf.keras.layers.Dense(1)(x00)
    OUT = tf.keras.layers.Activation('sigmoid')(x00)

    return tf.keras.Model(inputs=INP, outputs=OUT, name='DISCRIMINATOR')
  
# if __name__=="__main__":
#     d2 = Discriminator(
#          inputs_shape=(128,128,1), 
#          )
#     d2.summary()

#%% PatchDiscriminator Architecture

def PatchDiscriminator(
        inputs_shape, 
        target_shape,
        layer_N=[64, 96, 128, 160],
        input_stack_num=2, 
        pool=True, 
        activation='leaky',
        initializer = tf.random_normal_initializer(0., 0.02)
        ):
    
    INP = tf.keras.layers.Input(shape=inputs_shape, name='input_image')
    TAR = tf.keras.layers.Input(shape=target_shape, name='target_image')
    
    x01 = tf.keras.layers.Concatenate()([INP, TAR])
    
    # Encoder
    X_en1 = CONV_stack(x01, layer_N[0], kernel_size=3, stack_num=input_stack_num, activation=activation, name='disc_left0') 
    X_en2 = EncoderBlock(X_en1, layer_N[1], pool=pool, activation=activation, name='disc_left1')
    X_en3 = EncoderBlock(X_en2, layer_N[2], pool=pool, activation=activation, name='disc_left2')
    
    # Bottleneck
    X4 = EncoderBlock(X_en3, layer_N[3], pool=pool, activation=activation, name='disc_bottom')
    
    # Final output
    x00 = tf.keras.layers.BatchNormalization()(X4)
    x00 = tf.keras.layers.LeakyReLU()(x00)
    OUT = tf.keras.layers.Conv2D(1, 4, strides=1,
                                  kernel_initializer=initializer)(x00)

    return tf.keras.Model(inputs=[INP, TAR], outputs=OUT, name='PATCH-DISCRIMINATOR')
  
# if __name__=="__main__":
#     d2 = PatchDiscriminator(
#             inputs_shape=(128,128,7), 
#             target_shape=(128,128,1),
#             )
#     d2.summary()


#%% Other Models Network Construct Utilities

def stride_conv(X, channel, pool_size=2, activation='relu', name='X'):
    '''
    stride convolutional layer --> batch normalization --> Activation
    *Proposed to replace max- and average-pooling layers

    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        pool_size: size of stride
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU
        name: name of created keras layers

    Output
    ----------
        X: output tensor
    '''
    # linear convolution with strides
    X = tf.keras.layers.Conv2D(channel, pool_size, strides=(pool_size, pool_size), padding='valid',
                            use_bias=False, kernel_initializer='he_normal', name=name+'_stride_conv')(X)
    # batch normalization
    X = tf.keras.layers.BatchNormalization(axis=3, name=name+'_stride_conv_bn')(X)

    # activation
    if activation == 'relu':
        X = tf.keras.layers.ReLU(name=name+'_stride_conv_relu')(X)
    elif activation == 'leaky':
        X = tf.keras.layers.LeakyReLU(alpha=0.3, name=name+'_stride_conv_leaky')(X)
    elif activation == 'prelu':
            X = tf.keras.layers.PReLU(alpha_initializer='zeros', alpha_regularizer=None, alpha_constraint=None, shared_axes=[1, 2], name=name+'_stride_conv_prelu')(X)

    return X

def CONV_stack(X, channel, kernel_size=3, stack_num=2, activation='relu', name='conv_stac'):
    '''
    (Convolutional layer --> batch normalization --> Activation)*stack_num

    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        stack_num: number of stacked convolutional layers
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU
        name: name of created keras layers

    Output
    ----------
        X: output tensor

    '''

    # stacking Convolutional layers
    for i in range(stack_num):

        # linear convolution
        X = tf.keras.layers.Conv2D(channel, kernel_size, padding='same', use_bias=False,
                                kernel_initializer='he_normal', name=name+'_stack{}_conv'.format(i))(X)

        # batch normalization
        X = tf.keras.layers.BatchNormalization(axis=3, name=name+'_stack{}_bn'.format(i))(X)

        # activation
        if activation == 'relu':
            X = tf.keras.layers.ReLU(name=name+'_stack{}_relu'.format(i))(X)
        elif activation == 'leaky':
            X = tf.keras.layers.LeakyReLU(alpha=0.3, name=name+'_stack{}_leaky'.format(i))(X)
        elif activation == 'prelu':
            X = tf.keras.layers.PReLU(alpha_initializer='zeros', alpha_regularizer=None, alpha_constraint=None, shared_axes=[1, 2], name=name+'_stack{}_prelu'.format(i))(X)

    return X


def UNET_left(X, channel, kernel_size=3, pool_size=2, pool=True, activation='relu', name='left0'):
    '''
    Encoder block of UNet

    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        pool_size: size of stride
        pool: True for maxpooling, False for strided convolutional layers
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU
        name: name of created keras layers

    Output
    ----------
        X: output tensor

    '''

    # maxpooling layer vs strided convolutional layers
    if pool:
        X = tf.keras.layers.MaxPooling2D(pool_size=(pool_size, pool_size), name='{}_pool'.format(name))(X)
    else:
        X = stride_conv(X, channel, pool_size, activation=activation, name=name)

    # stack linear convolutional layers
    X = CONV_stack(X, channel, kernel_size, stack_num=1, activation=activation, name=name)

    return X

def UNET_right(X, X_left, channel, kernel_size=3, pool_size=2, activation='relu', name='right0'):
    '''
    Decoder block of UNet

    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        pool_size: size of transpose stride, expected to be the same as "UNET_left"
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU
        name: name of created keras layers

    Output
    ----------
        X: output tensor

    '''

    # Transpose convolutional layer --> stacked linear convolutional layers
    X = tf.keras.layers.Conv2DTranspose(channel, kernel_size, strides=(pool_size, pool_size),
                                     padding='same', name=name+'_trans_conv')(X)
    X = CONV_stack(X, channel, kernel_size, stack_num=1, activation=activation, name=name+'_conv_after_trans')

    # Tensor concatenation
    H = tf.keras.layers.concatenate([X_left, X], axis=3)

    # stacked linear convolutional layers after concatenation
    H = CONV_stack(H, channel, kernel_size, stack_num=1, activation=activation, name=name+'_conv_after_concat')

    return H

def XNET_right(X_conv, X_list, channel, kernel_size=3, pool_size=2, activation='relu', name='right0'):
    '''
    Decoder block of Nest-UNet

    Input
    ----------
        X: input tensor
        X_list: a list of other corresponded input tensors (see Sha 2020b, Figure 2)
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        pool_size: size of transpose stride, expected to be the same as "UNET_left"
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU
        name: name of created keras layers

    Output
    ----------
        X: output tensor

    '''

    # Transpose convolutional layer --> concatenation
    X_unpool = tf.keras.layers.Conv2DTranspose(channel, kernel_size, strides=(pool_size, pool_size),
                                            padding='same', name=name+'_trans_conv')(X_conv)

    # <--- *stacked convolutional can be applied here
    X_unpool = tf.keras.layers.concatenate([X_unpool]+X_list, axis=3, name=name+'_nest')

    # Stacked convolutions after concatenation
    X_conv = CONV_stack(X_unpool, channel, kernel_size, stack_num=2, activation=activation, name=name+'_conv_after_concat')

    return X_conv



#%% s01: SRDRN Architecture


#%% NEST_UNET Architecture

def NEST_UNET(lr_input_shape, 
              hr_input_shape=None, 
              ups_factors=(2,2,2), 
              layer_N=[64, 96, 128, 160],
              input_stack_num=2,
              pool=True,
              activation='prelu',
              n_classes=1,
              isgammaloss=False,
              ):
    '''
    Nest-UNet (or UNet++) with three down- and upsampling levels.
    '''
    # input layer
    IN_LR = tf.keras.layers.Input(lr_input_shape, name='unet_in_lr')
    
    x01 = IN_LR
    for _, ups_size in enumerate(ups_factors):
        x01 = tf.keras.layers.UpSampling2D(size=ups_size, interpolation='bilinear')(x01)
    if hr_input_shape is not None:
        # Concatenate the upsampled low resolution input and the high resolution input
        IN_HR = tf.keras.layers.Input(hr_input_shape, name='unet_in_hr')
        x = tf.keras.layers.concatenate([x01, IN_HR])    
    else:
        x = x01
    X11_conv = CONV_stack(x, layer_N[0], kernel_size=3, stack_num=input_stack_num, activation=activation, name='unet_left0')
    # downsampling levels (same as in the UNET)
    X21_conv = UNET_left(X11_conv, layer_N[1], pool=pool, activation=activation, name='unet_left1')
    X31_conv = UNET_left(X21_conv, layer_N[2], pool=pool, activation=activation, name='unet_left2')
    X41_conv = UNET_left(X31_conv, layer_N[3], pool=pool, activation=activation, name='unet_bottom')
    # up-sampling part 1
    X12_conv = XNET_right(X21_conv, [X11_conv], layer_N[0], activation=activation, name='xnet_12')
    X22_conv = XNET_right(X31_conv, [X21_conv], layer_N[1], activation=activation, name='xnet_22')
    X32_conv = XNET_right(X41_conv, [X31_conv], layer_N[2], activation=activation, name='xnet_32')
    # up-sampling part 2
    X13_conv = XNET_right(X22_conv, [X11_conv, X12_conv], layer_N[0], activation=activation, name='xnet_right13')
    X23_conv = XNET_right(X32_conv, [X21_conv, X22_conv], layer_N[1], activation=activation, name='xnet_right23')
    # up-sampling part 3
    X14_conv = XNET_right(X23_conv, [X11_conv, X12_conv, X13_conv], layer_N[0], activation=activation, name='xnet_right14')
    # output
    x =  CONV_stack(X14_conv, 16, kernel_size=3, stack_num=1, activation=activation, name='xnet_out')
    if isgammaloss:
        out1 = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                      activation='selu', padding='same', name='xnet_out1')(x)
        out2 = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                      activation='selu', padding='same', name='xnet_out2')(x)
        out3 = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                      activation='sigmoid', padding='same', name='xnet_out3')(x)
        OUT = tf.keras.layers.Concatenate()([out1, out2, out3])
        return tf.keras.models.Model(inputs=[IN_LR, IN_HR] if hr_input_shape is not None else [IN_LR], outputs=[OUT], name='NEST-UNET-x3')
    else:
        OUT = tf.keras.layers.Conv2D(kernel_size=n_classes, filters=1, 
                                     activation="linear", padding='same', name='unet_exit')(x)
        return tf.keras.models.Model(inputs=[IN_LR, IN_HR] if hr_input_shape is not None else [IN_LR], outputs=[OUT], name='NEST-UNET')
    
#%% u03: UNET_DENSE

def UNET_DENSE(lr_input_shape, hr_input_shape, ups_factors, 
               layer_N=[64, 96, 128, 160],
               input_stack_num=2, 
               n_dense = 256,
               drop_rate = 0.5, 
               pool=True, 
               activation='prelu',
               ):
    '''
    UNet with three down- and upsampling levels.
    '''
    
    IN_LR = tf.keras.layers.Input(lr_input_shape, name='unet_in_lr')
    IN_HR = tf.keras.layers.Input(hr_input_shape, name='unet_in_hr')
    
    x01 = IN_LR
    for _, ups_size in enumerate(ups_factors):
        x01 = tf.keras.layers.UpSampling2D(size=ups_size, interpolation='bilinear')(x01)
    
    # Concatenate the upsampled low resolution input and the high resolution input
    x = tf.keras.layers.concatenate([x01, IN_HR])

    
    X_en1 = CONV_stack(x, layer_N[0], kernel_size=3, stack_num=input_stack_num, activation=activation, name='unet_left0')
    
    # downsampling levels
    X_en2 = UNET_left(X_en1, layer_N[1], pool=pool, activation=activation, name='unet_left1')
    X_en3 = UNET_left(X_en2, layer_N[2], pool=pool, activation=activation, name='unet_left2')
    
    X4 = UNET_left(X_en3, layer_N[3], pool=pool, activation=activation, name='unet_bottom')

    # upsampling levels
    X_de3 = UNET_right(X4, X_en3, layer_N[2], activation=activation, name='unet_right2')
    X_de2 = UNET_right(X_de3, X_en2, layer_N[1], activation=activation, name='unet_right1')
    X_de1 = UNET_right(X_de2, X_en1, layer_N[0], activation=activation, name='unet_right0')
    
    
    # output
    model = CONV_stack(X_de1, 16, kernel_size=3, stack_num=1, activation=activation, name='unet_out')
    # Initiate Dense layers
    model = tf.keras.layers.Conv2D(1,1)(model)
    model = tf.keras.layers.PReLU()(model)
    model = tf.keras.layers.Flatten()(model)
    model = tf.keras.layers.Dense(n_dense)(model)
    model = tf.keras.layers.PReLU()(model)
    model = tf.keras.layers.Dropout(drop_rate)(model)
    model = tf.keras.layers.Dense(np.prod(ups_factors)*lr_input_shape[0]*np.prod(ups_factors)*lr_input_shape[1])(model)
    model = tf.keras.layers.Activation("linear")(model)
    OUT =tf. keras.layers.Reshape((np.prod(ups_factors)*lr_input_shape[0], np.prod(ups_factors)*lr_input_shape[1],1))(model)

    # model
    model = tf.keras.models.Model(inputs=[IN_LR, IN_HR], outputs=[OUT], name='UNET-DENSE')

    return model
#%% Extinct Versions

def UNET_o(input_shape, ups_factors, layer_N=[64, 96, 128, 160], mode='lrhr', input_stack_num=2, pool=True, activation='relu'):
    '''
    UNet with three down- and upsampling levels.

    Input
    ----------
        layer_N: Number of convolution filters on each down- and upsampling levels
                 Should be an iterable of four int numbers, e.g., [32, 64, 128, 256]

        input_shape: a tuple that feed input keras.layers.Input, e.g. (None, None, 3)

        input_stack_num: number of stacked convolutional layers before entering the first downsampling block

        pool: True for maxpooling, False for strided convolutional layers
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU

    Output
    ----------
        model: the Keras functional API model, i.e., keras.models.Model(inputs=[IN], outputs=[OUT])

    '''

    # input layer
    # input layer
    if mode=='lrhr':
        IN = x = tf.keras.layers.Input(input_shape, name='unet_in')
        for _, ups_size in enumerate(ups_factors):
            x = tf.keras.layers.UpSampling2D(size=ups_size, interpolation='bilinear')(x)
        
        X_en1 = CONV_stack(x, layer_N[0], kernel_size=3, stack_num=input_stack_num, activation=activation, name='unet_left0')
    
    elif mode=='hrhr':
        IN = tf.keras.layers.Input(input_shape, name='unet_in')
        X_en1 = CONV_stack(IN, layer_N[0], kernel_size=3, stack_num=input_stack_num, activation=activation, name='unet_left0')
        
    else:
        mode_options = "', '".join(["lrhr", "hrhr"])
        raise ValueError(f"Invalid upsampling method. Available options are '{mode_options}'.")
    
    # downsampling levels
    X_en2 = UNET_left(X_en1, layer_N[1], pool=pool, activation=activation, name='unet_left1')
    X_en3 = UNET_left(X_en2, layer_N[2], pool=pool, activation=activation, name='unet_left2')
    X4 = UNET_left(X_en3, layer_N[3], pool=pool, activation=activation, name='unet_bottom')

    # upsampling levels
    X_de3 = UNET_right(X4, X_en3, layer_N[2], activation=activation, name='unet_right2')
    X_de2 = UNET_right(X_de3, X_en2, layer_N[1], activation=activation, name='unet_right1')
    X_de1 = UNET_right(X_de2, X_en1, layer_N[0], activation=activation, name='unet_right0')

    # output
    OUT = CONV_stack(X_de1, 2, kernel_size=3, stack_num=1, activation=activation, name='unet_out')
    OUT = tf.keras.layers.Conv2D(1, 1, activation=tf.keras.activations.linear, padding='same', name='unet_exit')(OUT)

    # model
    model = tf.keras.models.Model(inputs=[IN], outputs=[OUT], name='UNet')

    return model

## NEST_UNET_o

def NEST_UNET_o(input_shape, ups_factors, layer_N=[64, 96, 128, 160], mode='lrhr', input_stack_num=2, pool=True, activation='relu'):
    '''
    Nest-UNet (or UNet++) with three down- and upsampling levels.

    Input
    ----------
        layer_N: Number of convolution filters on each down- and upsampling levels
                 Should be an iterable of four int numbers, e.g., [32, 64, 128, 256]

        input_shape: a tuple that feed input keras.layers.Input, e.g. (None, None, 3)
        input_stack_num: number of stacked convolutional layers before entering the first downsampling block
        activation: 'relu' for ReLU or 'leaky' for Leaky ReLU
        pool: True for maxpooling, False for strided convolutional layers

    Output
    ----------
        model: the Keras functional API model, i.e., keras.models.Model(inputs=[IN], outputs=[OUT])

    '''

    # input layer
    if mode=='lrhr':
        IN = x = tf.keras.layers.Input(input_shape, name='unet_in')
        for _, ups_size in enumerate(ups_factors):
            x = tf.keras.layers.UpSampling2D(size=ups_size, interpolation='bilinear')(x)
        
        X11_conv = CONV_stack(x, layer_N[0], kernel_size=3, stack_num=input_stack_num, activation=activation, name='unet_left0')
    
    elif mode=='hrhr':
        IN = tf.keras.layers.Input(input_shape, name='unet_in')
        X11_conv = CONV_stack(IN, layer_N[0], kernel_size=3, stack_num=input_stack_num, activation=activation, name='unet_left0')
        
    else:
        mode_options = "', '".join(["lrhr", "hrhr"])
        raise ValueError(f"Invalid upsampling method. Available options are '{mode_options}'.")

    # downsampling levels (same as in the UNET)
    X21_conv = UNET_left(X11_conv, layer_N[1], pool=pool, activation=activation, name='unet_left1')
    X31_conv = UNET_left(X21_conv, layer_N[2], pool=pool, activation=activation, name='unet_left2')
    X41_conv = UNET_left(X31_conv, layer_N[3], pool=pool, activation=activation, name='unet_bottom')

    # up-sampling part 1
    X12_conv = XNET_right(X21_conv, [X11_conv], layer_N[0], activation=activation, name='xnet_12')
    X22_conv = XNET_right(X31_conv, [X21_conv], layer_N[1], activation=activation, name='xnet_22')
    X32_conv = XNET_right(X41_conv, [X31_conv], layer_N[2], activation=activation, name='xnet_32')

    # up-sampling part 2
    X13_conv = XNET_right(X22_conv, [X11_conv, X12_conv], layer_N[0], activation=activation, name='xnet_right13')
    X23_conv = XNET_right(X32_conv, [X21_conv, X22_conv], layer_N[1], activation=activation, name='xnet_right23')

    # up-sampling part 3
    X14_conv = XNET_right(X23_conv, [X11_conv, X12_conv, X13_conv], layer_N[0], activation=activation, name='xnet_right14')

    # output
    OUT = CONV_stack(X14_conv, 2, kernel_size=3, stack_num=1, activation=activation, name='xnet_out')
    OUT = tf.keras.layers.Conv2D(1, 1, activation=tf.keras.activations.linear)(OUT)

    # model
    model = tf.keras.models.Model(inputs=[IN], outputs=[OUT], name='Nest-UNet')

    return model