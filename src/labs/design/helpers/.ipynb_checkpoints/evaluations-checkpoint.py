#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:28:44 2020

@author: scahyo
"""
import math
import numpy as np

class Evaluation:
    def __init__(self, x: np.ndarray, y: np.ndarray, *args, **kwargs):
        self.x = x.reshape(x.shape[0])
        self.y = y.reshape(x.shape[0])

    def mda(self, *args, **kwargs):
        return round(np.mean(
            np.sign(self.x[1:] - self.x[:-1]) == np.sign(self.y[1:] - self.y[:-1])
        ), 3)
        
    def mae(self, *args, **kwargs): 
        #x = measure, y = predict 
        result = 0 
        for i in range(len(self.x)): 
            result += abs(self.x[i] - self.y[i]) 
        return round(result/len(self.x), 3)

    def rmse(self, *args, **kwargs): 
        #x=measure, y=predict 
        result=0 
        for i in range(len(self.x)): 
            result += (self.x[i] - self.y[i])**2
        result = result/len(self.x)
        return round(math.sqrt(result), 3)