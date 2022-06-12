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

import matplotlib.pyplot as plt

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
        self.train_accurate=accuracy_score(self.model.predict(self.X), self.Y)
        self.test_accurate=accuracy_score(self.model.predict(self.Test_X), self.Test_Y)

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, fileData):
        self._data=pd.read_csv(fileData,header=None)
        self.Xnp=self._data.drop(columns=60,axis=1)
        self.Ynp=self._data[60]
        self.X, self.Test_X, self.Y, self.Test_Y= train_test_split(self.Xnp,self.Ynp,test_size=0.1,stratify=self.Ynp, random_state=1)
    
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
        return f'the model has a train accuracy score of {self.train_accurate} with a test accuracy score of {self.test_accurate}'
        
Sonar=Model('data.csv')
def test():
    int_data = (0.0307,0.0523,0.0653,0.0521,0.0611,0.0577,0.0665,0.0664,0.1460,0.2792,0.3877,0.4992,0.4981,0.4972,0.5607,0.7339,0.8230,0.9173,0.9975,0.9911,0.8240,0.6498,0.5980,0.4862,0.3150,0.1543,0.0989,0.0284,0.1008,0.2636,0.2694,0.2930,0.2925,0.3998,0.3660,0.3172,0.4609,0.4374,0.1820,0.3376,0.6202,0.4448,0.1863,0.1420,0.0589,0.0576,0.0672,0.0269,0.0245,0.0190,0.0063,0.0321,0.0189,0.0137,0.0277,0.0152,0.0052,0.0121,0.0124,0.0055)
    Sonar.Predict(int_data)
    print(Sonar)
    return
test()





"""
A=pd.read_csv('data.csv',header=None)

A[60].value_counts().plot(kind='barh', color='blue')
plt.show()

# print one row for the 59 columns
for i in range(len(A)):
    moy = A.iloc[i,0:60].mean()
    if A.iloc[i,60] == 'M':
        pass
        #plt.hist(moy,color='red')
    else:
        plt.hist(moy,color='blue')
print(moy)




with open('data.csv', 'r') as f:
    O=f.read().splitlines()
    f.close()
A=[]
print()
for f in range(len(O)):
    D=[]
    G=O[f].split(',')
    for j in G:
        try:
            D.append(float(j))
        except ValueError:
            D.append(j)
    A.append(D)
    
A=np.array(A)
A_R=[]
for i in range(len(A[0])):
    moy=0
    for j in range(97):
        moy+=A[j][i]
    moy=moy/97
    A_R.append(moy)
A_M=[]
for i in range(len(A[0])):
    moy=0
    for j in range(97,len(A)):
        moy+=A[j][i]
    moy=moy/(len(A)-97)
    A_M.append(moy)

print(type(A[0]))


#B=[x for x in range(len(A[0]))]
plt.plot(1,A_R,"b")
plt.plot(0,A_M,"r")
plt.plot(B,[0.0307,0.0523,0.0653,0.0521,0.0611,0.0577,0.0665,0.0664,0.1460,0.2792,0.3877,0.4992,0.4981,0.4972,0.5607,0.7339,0.8230,0.9173,0.9975,0.9911,0.8240,0.6498,0.5980,0.4862,0.3150,0.1543,0.0989,0.0284,0.1008,0.2636,0.2694,0.2930,0.2925,0.3998,0.3660,0.3172,0.4609,0.4374,0.1820,0.3376,0.6202,0.4448,0.1863,0.1420,0.0589,0.0576,0.0672,0.0269,0.0245,0.0190,0.0063,0.0321,0.0189,0.0137,0.0277,0.0152,0.0052,0.0121,0.0124,0.0055],"c" )
plt.plot(B,[0.0373,0.0281,0.0232,0.0225,0.0179,0.0733,0.0841,0.1031,0.0993,0.0802,0.1564,0.2565,0.2624,0.1179,0.0597,0.1563,0.2241,0.3586,0.1792,0.3256,0.6079,0.6988,0.8391,0.8553,0.7710,0.6215,0.5736,0.4402,0.4056,0.4411,0.5130,0.5965,0.7272,0.6539,0.5902,0.5393,0.4897,0.4081,0.4145,0.6003,0.7196,0.6633,0.6287,0.4087,0.3212,0.2518,0.1482,0.0988,0.0317,0.0269,0.0066,0.0008,0.0045,0.0024,0.0006,0.0073,0.0096,0.0054,0.0085,0.0060],"g" )
plt.show()

plt.show()
"""