# Training the Network

'''
Creates the models based on the corpora
Runs only if models don't exist
'''

# ---------------------------------------------------------------------------------------------------------------------
# Imports

import os
import pickle
import json
import numpy
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

# ---------------------------------------------------------------------------------------------------------------------
# Data Functions

def get_corpus_data(corpus_file):
    words = []
    word_classes = []
    docs = []
    corpus = json.loads(open(f'{current_path}/corpora/{corpus_file}').read())
    for intent in corpus['intents']:
        for pattern in intent['patterns']:
            pattern_words = nltk.word_tokenize(pattern)
            words.extend(pattern_words)
            docs.append((pattern_words, intent['tag']))
            if intent['tag'] not in word_classes:
                word_classes.append(intent['tag'])
    save_data(words, word_classes, docs, corpus_file)
    
def save_data(words_lst, word_classes_lst, docs_lst, corpus_file):
    corpus_name = str(corpus_file).strip('.json')
    words = sorted(set([lemmatiser.lemmatize(str(word).lower()) for word in words_lst if word not in ignore_chrs]))
    word_classes = sorted(set(word_classes_lst))
    pickle.dump(words, open(f'models/{corpus_name}_words.pkl', 'wb'))
    pickle.dump(word_classes, open(f'models/{corpus_name}_classes.pkl', 'wb'))
    create_training_data(words, word_classes, docs_lst)
    
# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def training_main():
    for i in range(len(corpora)):
        get_corpus_data(corpora[i])

# ---------------------------------------------------------------------------------------------------------------------
# Globals

current_path = os.getcwd()
corpora = [file for file in os.listdir(f'{current_path}/corpora/') if file.endswith('.json')]
lemmatiser = WordNetLemmatizer()
ignore_chrs = ['?', '!', '.', ',', "'", '"', '/', '£', '$', 
                '%', '^', '&', '*', '@', ':', ';', '#', '~', 
                '|', '<', '>', '{', '}', '_', '-', '+', '='
]

# ---------------------------------------------------------------------------------------------------------------------
# Runs File

if __name__ == '__main__':
    training_main()
