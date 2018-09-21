
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 04 19:39:57 2018

@author: user
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            """
import keras
from keras.datasets import mnist
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Flatten, Input, Reshape
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import numpy as np 

batch_size = 128
num_classes = 10
epochs = 12

# input image dimensions
img_rows, img_cols = 28, 28

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train_flat = np.array([i.reshape((784))for i in x_train]) 

x_test_flat = np.array([i.reshape((784))for i in x_test]) 

y_train_one_hot = keras.utils.to_categorical(y_train) 

y_test_one_hot = keras.utils.to_categorical(y_test) 
 

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1) 

x_test = x_test.reshape(x_test.shape[0], 28, 28, 1) 


inp = Input(shape=(28,28,1)) 

#inp = Reshape((28,28,1))(inp) 

conv = Conv2D(32, (3,3), activation='sigmoid')(inp) 

pool = MaxPooling2D((2,2))(conv) 

  

flat = Flatten()(pool) 

hid = Dense(100, activation='sigmoid')(flat) 

out = Dense(10, activation='sigmoid')(hid) 

  

model = Model([inp],out) 

model.compile(loss='mse', optimizer='adam',metrics=['accuracy']) 

model.fit(x_train,y_train_one_hot,epochs=10,verbose=2)
