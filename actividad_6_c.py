# -*- coding: utf-8 -*-
"""Actividad_6_C.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xartugzaioKO9H9eGpUr2I6PJjnUdmMb
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('2.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

th, img_bn = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY_INV)
img_bn = cv2.resize(img_bn,(28,28))

plt.imshow(img_bn,cmap=plt.cm.gray)
plt.show()

x = img_bn.reshape(1,784)

import pickle
#Cargando los modelos guardados
SVM = pickle.load(open('SVM_mnist_784.sav','rb'))
MLP = pickle.load(open('MLP_mnist_784.sav','rb'))

y_SVM = SVM.predict(x)
y_MLP = MLP.predict(x)

plt.figure()
plt.imshow(img_bn,cmap=plt.cm.gray)
plt.title('Prediction SVM: ' + str(y_SVM))
plt.show()

plt.figure()
plt.imshow(img_bn,cmap=plt.cm.gray)
plt.title('Prediction MLP: ' + str(y_MLP))
plt.show()