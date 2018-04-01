# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:06:14 2018

@author: Shiva
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

#formula obtained for the trained model
def graph(formula, x_range):
   x = np.array(x_range)
   y = eval(formula)
   plt.plot(x, y)

if __name__ == '__main__':

    x = [0, 1, 2, 3, 4, 5, 6]
    y = [0, 2, 4, 6, 8, 10, 12]

    x_random = np.random.randn(len(x)) * 0.01;

    x = x + x_random
    size2 = np.array(x).reshape((-1, 1))
    
    #fitting into the model
    regr = linear_model.LinearRegression()
    regr.fit(size2, y)
    
    print('Coefficients: \n', regr.coef_)
    print('intercept: \n', regr.intercept_)
        
    #plotting the prediction line    
    graph('regr.coef_*x + regr.intercept_', range(1, 20))
    print regr.score(size2, y)
    
    plt.scatter (x, y, color='black')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.show()
