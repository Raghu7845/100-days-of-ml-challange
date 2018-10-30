# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:53:31 2018

@author: raghup
"""

import pandas as pd
import numpy as np
df = pd.read_csv('Salary_data.csv')
train_len = df.shape[0]/3

df.insert(0,0,1)
idvs = df.iloc[:train_len*2,:-1]
x_max = idvs.max(axis=0)
idv1 = idvs/x_max
y_max = df.iloc[:,-1].max(axis=0)
tv = df.iloc[:train_len*2,-1]
X = idv1.values
Y = tv.values
Y = np.reshape(Y,(len(Y),1))
theta = np.array([0 for i in range(len(X[0]))]).astype(np.float)
theta = np.reshape(theta ,(1,len(X[0])))


import LinearModel
LM = LinearModel.LinearModel()




pred1 = LM.fit(alpha=0.06,X=X,Y=Y,theta=theta,steps =5000)
th = LM.value_theta = []
validate = df.iloc[train_len:,:-1]
res = df.iloc[train_len:,-1]
validate/=x_max
validate = validate.values

result = LM.predict(validate)
res1 = np.dot(pred1,validate.T)
res1.shape[1]
res1 = pd.Series(np.reshape(res1,(res1.shape[1],)))

import matplotlib.pyplot as plt
plt.plot(range(len(res1)),res1,color='red',label = 'created model(predicted)')
plt.scatter(range(len(res)),res,color='blue',label = 'original')
plt.legend(loc='upper right')
plt.savefig('LinearModel')
plt.show()
plt.close()

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df.iloc[:train_len*2,:-1],df.iloc[:train_len*2,-1])
out = model.predict(df.iloc[train_len:,:-1])
plt.plot(out,color='green',label = 'sklearn model(predicted)')
plt.scatter(range(len(res)),res,color='blue',label = 'original')
plt.legend(loc='upper right')
plt.savefig('sklearn model')
plt.show()
plt.close()