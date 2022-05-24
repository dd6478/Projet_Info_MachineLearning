#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:25:27 2022

@author: baby-ghost
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

##### Projet Info #####


### Initialisation ###
'''
Data = pd.read_csv('data.csv', header=None)
X=Data.drop(columns=60,axis=1) #sup la dernière colone
Y=Data[60] #sup tout les autre colone sauf la dernière (c la qui ya ecrit si c une mine ou une pierre)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=1)

### Training model ###
model = LogisticRegression()
model.fit(X_train, Y_train)

### Predictive System ###
#int_data = (0.0307,0.0523,0.0653,0.0521,0.0611,0.0577,0.0665,0.0664,0.1460,0.2792,0.3877,0.4992,0.4981,0.4972,0.5607,0.7339,0.8230,0.9173,0.9975,0.9911,0.8240,0.6498,0.5980,0.4862,0.3150,0.1543,0.0989,0.0284,0.1008,0.2636,0.2694,0.2930,0.2925,0.3998,0.3660,0.3172,0.4609,0.4374,0.1820,0.3376,0.6202,0.4448,0.1863,0.1420,0.0589,0.0576,0.0672,0.0269,0.0245,0.0190,0.0063,0.0321,0.0189,0.0137,0.0277,0.0152,0.0052,0.0121,0.0124,0.0055)
int_data = (0.0307,0.0523,0.0653,0.0521,0.0611,0.0577,0.0665,0.0664,0.1460,0.2792,0.3877,0.2992,0.4981,0.4972,0.5607,0.7339,0.8230,0.9173,0.9975,0.9911,0.8240,0.6498,0.5980,0.4862,0.3150,0.1543,0.0989,0.0284,0.1008,0.2636,0.2694,0.2930,0.2925,0.3998,0.3660,0.3172,0.4609,0.4374,0.1820,0.3376,0.6202,0.4448,0.1863,0.1420,0.0589,0.0576,0.0672,0.0269,0.0245,0.0190,0.0063,0.0321,0.0189,0.0137,0.0277,0.0152,0.0052,0.0121,0.0124,0.0055)
int_data = np.asarray(int_data)
int_data = int_data.reshape(1,-1)

if model.predict(int_data) == 'M':
    print("l'objet est une mine")
else:
    print("l'objet est une pierre")
'''

### Class Method ###

class Model:
    def __init__(self, fileData):
        self.data=fileData
        self.model=LogisticRegression()
        self.model.fit(self.X,self.Y)
        self.accurate=accuracy_score(self.model.predict(self.X), self.Y)

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, fileData):
        self._data=pd.read_csv(fileData,header=None)
        self.X, Test_X, self.Y, Test_Y= train_test_split(self._data.drop(columns=60,axis=1),self._data[60],test_size=0.1,stratify=self._data[60], random_state=1)
    
    def changeInputData(self,data):
        data = np.asarray(data)
        return data.reshape(1,-1)
    
    def Predict(self, input_data):
        data=self.changeInputData(input_data)
        if self.model.predict(data) == 'M':
            print('the object is an Mine')
        else :
            print('the object is an Rock')
        
    def __str__(self):
        return f'le model a une precision de {self.accurate}'
        
Sonar=Model('data.csv')
def test():
    int_data = (0.0307,0.0523,0.0653,0.0521,0.0611,0.0577,0.0665,0.0664,0.1460,0.2792,0.3877,0.4992,0.4981,0.4972,0.5607,0.7339,0.8230,0.9173,0.9975,0.9911,0.8240,0.6498,0.5980,0.4862,0.3150,0.1543,0.0989,0.0284,0.1008,0.2636,0.2694,0.2930,0.2925,0.3998,0.3660,0.3172,0.4609,0.4374,0.1820,0.3376,0.6202,0.4448,0.1863,0.1420,0.0589,0.0576,0.0672,0.0269,0.0245,0.0190,0.0063,0.0321,0.0189,0.0137,0.0277,0.0152,0.0052,0.0121,0.0124,0.0055)
    Sonar.Predict(int_data)
    return
test()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
