# ai4klim/__init__.py
import os
import logging
import sys

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Suppress specific TensorFlow logs and warnings
logging.getLogger('tensorflow').setLevel(logging.ERROR)

# Suppress stderr output (optional)
sys.stderr = open(os.devnull, 'w')

from .tensorflow import losses, train, models, utils

