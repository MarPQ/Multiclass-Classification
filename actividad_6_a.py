# -*- coding: utf-8 -*-
"""Actividad_6_A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GLAaotEV2wbfj5V61gWJBF81z8qqVZeN
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Sensor.csv')
#print(data)

x = np.asanyarray(data.drop(columns=['D']))
y = np.asanyarray(data[['D']])
#print('\n',y)

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1)

def resultados (model,x_test,y_test):
  y_pred = model.predict(x_test)

  print('Metricas: \n', metrics.classification_report(y_test,y_pred))
  print('matriz de confusion: \n', metrics.confusion_matrix(y_test,y_pred))

from sklearn.svm import SVC

model = Pipeline([('scaler', StandardScaler()),('cla',SVC())])
model.fit(x_train,y_train.ravel())

print('Train score: ', model.score(x_train, y_train))
print('Test score: ', model.score(x_test, y_test))

resultados(model,x_test,y_test)

from sklearn.neural_network import MLPClassifier

model = Pipeline([('scaler', StandardScaler()),('cla',MLPClassifier())])
model.fit(x_train,y_train.ravel())

print('Train score: ', model.score(x_train, y_train))
print('Test score: ', model.score(x_test, y_test))

resultados(model,x_test,y_test)