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
import json
import numpy
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

# ---------------------------------------------------------------------------------------------------------------------
# Data Functions

def get_data(corpus_file):
    pass

def call_tm():
    for i in range(len(corpora)):
        training_main(corpora[i])

# ---------------------------------------------------------------------------------------------------------------------
# Globals

current_path = os.getcwd()
corpora = [file for file in os.listdir(f'{current_path}/corpora/') if file.endswith('.json')]
lemmatiser = WordNetLemmatizer()
ignore_chrs = ['?', '!', '.', ',', "'", '"', '/', '£', '$', 
                '%', '^', '&', '*', '@', ':', ';', '#', '~', 
                '|', '<', '>', '{', '}', '_', '-', '+', '='
]




