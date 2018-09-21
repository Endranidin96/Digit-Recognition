# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 04:27:05 2018

@author: adi
"""

from keras.datasets import mnist
from sklearn import neighbors
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("done")
x_train_flat = np.array([i.reshape((784))for i in x_train])
x_test_flat = np.array([i.reshape((784))for i in x_test])
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train_flat,y_train)
predic = knn.predict(x_test_flat)
correct = 0
for i in range(len(y_test)):
    if predic[i]==y_test[i]:
        correct+=1
        
print("Accuracy: ",float(correct)/len(Y_test)*100)
#accuracy = 97.189        
