# Training the Network

'''
Creates the models based on the corpora
Runs only if models don't exist
'''

# ---------------------------------------------------------------------------------------------------------------------
# Imports

import os
import random
import pickle
import random
import numpy
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
