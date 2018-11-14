# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:09:35 2018

@author: raghup
"""

import pandas as pd
import numpy as np
df = pd.read_csv('50_Startups.csv')

df.head()
desc = df.describe()

for i in desc.columns:
    if desc[i]['std'] == 0:
        df = df.drop(i,axis=1)
df.columns
unique_states = list(df['State'].unique())

X = df.iloc[:,:-1].values
Y = df.iloc[:,-1].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X= onehotencoder.fit_transform(X).toarray()

X = X[:, 1:]

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

x1 = X_train[:]
from sklearn.preprocessing import MinMaxScaler
sc_X = MinMaxScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


y_pred = regressor.predict(X_test)


import matplotlib.pyplot as plt
plt.plot(range(len(y_pred)),y_pred,color='red',label = 'predicted')
plt.scatter(range(len(y_test)),y_test,color='blue',label = 'original')
plt.legend(loc='upper right')
#plt.savefig('Multiple Linear Regression')
plt.show()
plt.close()