# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:40:58 2018

@author: raghup
"""

import pandas as pd


df = pd.read_csv('Social_Network_Ads.csv')
X = df.iloc[:,0:-1].values
y = df.iloc[:,-1].values


from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder = LabelEncoder()
X[:, 1] = labelencoder.fit_transform(X[:, 1])
onehotencoder = OneHotEncoder(categorical_features = [1])
X= onehotencoder.fit_transform(X).toarray()

X = X[:,1:]


from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.7)


from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()
X_train = minmax.fit_transform(X_train)
X_test = minmax.transform(X_test)


from sklearn.svm import SVC
from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesClassifier
model = SVC(kernel = 'linear')
rfe = RFE(model,4)#X_train.shape[1])
rfe.fit(X_train,y_train)
rfe.ranking_
rfe.n_features_
rfe.support_


predicted = rfe.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,predicted)

