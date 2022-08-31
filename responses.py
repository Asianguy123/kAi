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
    message_words = message_clean_up(message_text)
    bag = [0] * len(words)
    for m_word in message_words:
        for i, word in enumerate(words):
            if word == m_word:
                bag[i] = 1
    return numpy.array(bag)

# ---------------------------------------------------------------------------------------------------------------------
# Response Retrieval Functions

def get_probabilities(message_text, words, model):
    bag_of_words = bow(message_text, words)
    prediction = model.predict(numpy.array([bag_of_words]))[0]
    results = [[i, result] for i, result in enumerate(prediction) if result > ERROR_THRESHOLD]
    return results

def get_class(results, word_classes):
    results.sort(key=lambda x:x[1], reverse=True)
    class_index = results[0][0]
    class_tag = word_classes[class_index]
    return class_tag

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
