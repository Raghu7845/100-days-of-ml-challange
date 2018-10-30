# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:47:01 2018

@author: Raghu
"""
import numpy as np
value_theta = []
class LinearModel:
    _coeff = None
    def check_rse(self,theta,X,Y,alpha):
        '''
            updating the value of theta
        '''
        res = np.dot(theta,X.T)
        res1 = res - Y[:,0]
        #print res1.shape
        res2 = [res1*X[:,i] for i in range(theta.shape[1])]
        sum1 = [np.sum(j)/len(X) for j in res2]
        some = alpha
        dot_prod = np.dot(sum1,some)
        theta = theta - dot_prod
        return theta
    
    def fit(self,alpha=1,X = [],Y = [],theta = [],steps=500):
        iter1 = 0
        while iter1<=steps:
            value_theta.append(theta)
            theta = self.check_rse(theta,X,Y,alpha)
            iter1+=1
        self._coeff = theta[:]
        return theta
    
    def predict(self,value):
        return np.dot(self._coeff,value.T)
    
