# -*- coding: utf-8 -*-
"""Actividad_6_B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AqOaux-WbaPr8JjwjX4fx1AfNHoCAzpL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('mnist_784.csv')
print(data)

x = np.asanyarray(data.drop(columns=['class']))
y = np.asanyarray(data[['class']])

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import metrics

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1)

def resultados (model,x_test,y_test):
  y_pred = model.predict(x_test)

  print('Metricas: \n', metrics.classification_report(y_test,y_pred))
  print('matriz de confusion: \n', metrics.confusion_matrix(y_test,y_pred))

from sklearn.svm import SVC

model = Pipeline([('scaler', StandardScaler()),('PCA',PCA(n_components=50)),('cla',SVC(C=0.82))])
model.fit(x_train,y_train.ravel())

print('Train score: ', model.score(x_train, y_train))
print('Test score: ', model.score(x_test, y_test))

resultados(model,x_test,y_test)

import pickle
#Guardando el modelo
pickle.dump(model,open('SVM_mnist_784.sav','wb'))

import pickle
#Cargando el modelo guardado
model = pickle.load(open('SVM_mnist_784.sav','rb'))

print('Train score: ', model.score(x_train, y_train))
print('Test score: ', model.score(x_test, y_test))

resultados(model,x_test,y_test)

from sklearn.neural_network import MLPClassifier

model = Pipeline([('scaler', StandardScaler()),('PCA',PCA(n_components=50)),('cla',MLPClassifier(hidden_layer_sizes=(500,500),alpha=0.01,max_iter=1500))])
model.fit(x_train,y_train.ravel())

print('Train score: ', model.score(x_train, y_train))
print('Test score: ', model.score(x_test, y_test))

resultados(model,x_test,y_test)

import pickle
#Guardando el modelo
pickle.dump(model,open('MLP_mnist_784.sav','wb'))

import pickle
#Cargando el modelo guardado
model = pickle.load(open('MLP_mnist_784.sav','rb'))

print('Train score: ', model.score(x_train, y_train))
print('Test score: ', model.score(x_test, y_test))

resultados(model,x_test,y_test)