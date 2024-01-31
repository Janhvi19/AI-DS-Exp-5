# -*- coding: utf-8 -*-
"""naiveBayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mAkk-Boh2aCwuSFmdy5WghEMeHsQKQbU
"""

import os

print(os.listdir())

# Commented out IPython magic to ensure Python compatibility.
# importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#to get graphs inline
# %matplotlib inline

dataSet = pd.read_csv('Social_Network_Ads.csv')

dataSet.info()

dataSet.head()

# spliting data into dependent and independent matrix
X = dataSet.iloc[:,2:4].values
y = dataSet.iloc[:,4].values

X

y

# splitting data into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

X_test

y_test

# feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()

classifier.fit(X_train, y_train)

y_predict = classifier.predict(X_test)

y_predict

from sklearn.metrics import confusion_matrix
falseCaci = confusion_matrix(y_test, y_predict)

falseCaci