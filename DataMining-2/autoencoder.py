# -*- coding: utf-8 -*-
"""autoencoder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T5IARpEmCcQfW51crNW0FgqbgrlkR8W3
"""

from keras.layers import Input, Dense
from keras.models import Model
from numpy import genfromtxt
from sklearn.model_selection import train_test_split

data = genfromtxt('normalized.csv',delimiter = ',')

print(data.shape)

encoding_dim =5  
input_img = Input(shape=(38,))
encoded = Dense((encoding_dim), activation='relu')(input_img)
decoded = Dense(38, activation='relu')(encoded)

autoencoder = Model(input_img, decoded)

encoder = Model(input_img, encoded)

encoded_input = Input(shape=(encoding_dim,))
# retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]
# create the decoder model
decoder = Model(encoded_input, decoder_layer(encoded_input))

autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

autoencoder.fit(data,data,
                epochs=100,
                batch_size=100,
                shuffle=True)

import matplotlib.pyplot as plt

encoded_imgs = encoder.predict(data)

print(encoded_imgs.shape)