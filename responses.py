# Finds Response

'''
Takes input from cwi.py and passes into model
Best response is gained
Response outputted to cwi.py for display
'''

# ---------------------------------------------------------------------------------------------------------------------
# Imports

import os
import pickle
import random
import json
import numpy
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def responses_main(model_name):
    pass
    
# ---------------------------------------------------------------------------------------------------------------------
# Globals

current_path = os.getcwd()
lemmatiser = WordNetLemmatizer()
