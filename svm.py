# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 05:01:58 2018

@author: adi
"""

import numpy as np
from sklearn import svm
x_mat = np.load('x.npy')
y_mat = np.load('y.npy')
X_train = x_mat[:50000]
Y_train = y_mat[:50000]
X_test = x_mat[50000:60000]
Y_test = y_mat[50000:60000]

digit_model = svm.SVC(kernel='poly')
digit_model.fit(X_train,Y_train)
predic = digit_model.predict(X_test)
correct = 0
for i in range(len(Y_test)):
    if predic[i]==Y_test[i]:
        correct+=1
print("Accuracy: ",float(correct)/len(Y_test)*100) 
#accuracy = 97.839   
