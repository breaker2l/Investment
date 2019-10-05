#import libraries
import numpy as np 
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel('D://Python/Data_files/housing.xlsx)

data

#Multivariate regression:
#In dependent variables:"house size","Number of rooms","Year of construction"

X = data[["house size","Number of rooms","Year of construction"]]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

reg.summary()

X = data[["house size","Number of rooms"]]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

reg.summary()

