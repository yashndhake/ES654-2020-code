import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from linearRegression.linearRegression import LinearRegression
from metrics import *
red = pd.read_excel('https://archive.ics.uci.edu/ml/machine-learning-databases/00477/Real%20estate%20valuation%20data%20set.xlsx')
newred = red.drop(['No'], axis=1)
shs = X.shape[0]//5
for fit_intercept in [True, False]:
    for i in range(5):
        yo = newred.loc[shs*i:shs*(i+1)].reset_index(drop=True)
        Xo=newred.drop(yo.index).reset_index(drop=True)
        y=Xo['Y house price of unit area']
        X= Xo.drop(['Y house price of unit area'], axis=1)
        yt=yo['Y house price of unit area']
        Xt= yo.drop(['Y house price of unit area'], axis=1)
        LR = LinearRegression(fit_intercept=fit_intercept)
        LR.fit(X, y)
        y_hat = LR.predict(Xt)
        LR.plot_residuals()
        y_hat = pd.Series(y_hat)
        print('RMSE: ', rmse(y_hat, y))
        print('MAE: ', mae(y_hat, y))
