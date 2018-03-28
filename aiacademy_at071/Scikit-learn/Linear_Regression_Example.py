# Loading Dataset & Quick Overview

import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn import metrics
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 15
data = load_boston()
print(data.keys())

print(data.data.shape) # data.data ==> Features
print(data.target.shape) # data.target ==> Label

print(data.DESCR)

# Plot Features V.S. Y

##練習對所有feature vs y 畫出散佈圖
"""
- CRIM     per capita crime rate by town
- ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
- INDUS    proportion of non-retail business acres per town
- CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- NOX      nitric oxides concentration (parts per 10 million)
- RM       average number of rooms per dwelling
- AGE      proportion of owner-occupied units built prior to 1940
- DIS      weighted distances to five Boston employment centres
- RAD      index of accessibility to radial highways
- TAX      full-value property-tax rate per $10,000
- PTRATIO  pupil-teacher ratio by town
- B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
- LSTAT    % lower status of the population
"""

for i in range(13):
    plt.subplot(4,4,i+1)
    plt.plot(data.data[:,i], data.target,'.',c='blue')
    plt.title(data.feature_names[i])

# Predicting Home Prices: Simple Linear Regression

