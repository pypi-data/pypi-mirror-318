# **DeepClimate**

*A Python package for climate modelling and data analysis with deep learning.*

**Latest Version:** 0.1.0
**Status:** Alpha

## **Description** 

[**DeepClimate**](https://pypi.org/project/deepclimate) is an intuitive Python library designed to simplify the training and evaluation of deep neural networks tailored for climate science. Whether you're working on emulation, downscaling, or bias correction of climate datasets, DeepClimate offers tools and pre-built deep learning models to accelerate your research and applications.

# Installing the package
```bash
pip install deepclimate
```

## **Features**  
- Built-in support for state-of-the-art deep learning architectures and training strategies (e.g., CNN, U-Net, GAN, etc.).  
- Custom loss functions for climate modeling and other climate-specific metrics.  
- Tools for data preprocessing, visualization, and evaluation.    

### **Objectives:**
1. Easy-to-use interface for novice users.
2. Develop a deep learning framework for training deep learning models with climate data.
3. Create custom modules for physics-informed training of deep learning models.
4. Custom training loss functions and evaluation metrics related to the climate science community.
5. An open library to host deep learning architectures from the literature.

### **Applications:**
- Climate data downscaling and bias-correction
- Weather/Climate prediction models.
- Hydro-meteorological research.
- Climate data analysis

### **Basic usage**

```python
# Import library modules
from deepclimate.tensorflow.train import ModelTraining
from deepclimate.tensorflow.models import LINEAR_DENSE
from deepclimate.tensorflow.losses import MeanAbsoluteError

# Load training and validation data
X_train, y_train = ...                # Prepare the training dataset (numpy array, Shape:[T x W x H x C])
X_val,   y_val   = ...                # Prepare the validation dataset (numpy array, Shape:[T x W x H x C])

model = LINEAR_DENSE(...)             # Construct the model architecture

# Initialize the ModelTraining class with specified parameters
mt = ModelTraining(
    generator = model,                # Generator architecture (model) to be used
    loss_fn   = MeanAbsoluteError(),  # Loss function for training 
    lr_init   = 0.0001,               # Initial learning rate for the optimizer
    )

# Train the model using the specified training and validation data, and other parameters
mt.train(
    train_data = (X_train, y_train),  # Training data (input features and target labels)
    val_data   = (X_val, y_val),      # Validation data (input features and target labels)
    epochs     = 10,                  # Number of epochs to train the model (can be adjusted)
    batch_size = 32,                  # Batch size for training and validation
    )
```

### **IMPORTANT NOTE**
- The package is under development. Stay connected.

