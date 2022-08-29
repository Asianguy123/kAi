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
# BOW Functions

def message_clean_up(message_text):
    message_words = nltk.word_tokenize(message_text)
    message_words = [lemmatiser.lemmatize(word) for word in message_words]
    return message_words

def bow(message_text, words):
    pass

# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def responses_main(model_name, message_text):
    words = pickle.load(open(f'models/{model_name}_words.pkl', 'rb'))
    words_classes = pickle.load(open(f'models/{model_name}_classes.pkl', 'rb'))
    model = load_model(f'models/{model_name}_model.h5')
    corpus = json.loads(open(f'corpora/{model_name}.json').read())

    get_probabilities(message_text, words, model)

# ---------------------------------------------------------------------------------------------------------------------
# Globals

current_path = os.getcwd()
lemmatiser = WordNetLemmatizer()
ERROR_THRESHOLD = 0.1

responses_main('dummy', 'hello')
