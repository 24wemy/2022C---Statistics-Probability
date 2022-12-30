# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:21:00 2022
@author: Ogi Wemy

"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

PATH = "D:/exercise/";
df = pd.read_csv(PATH+'book2.csv', usecols=['rata-rata suhu ruangan','jumlah cacat'])

df.head()
df.shape
df.info()
df.describe()
df.isnull().sum()

x = df['rata-rata suhu ruangan'].values.reshape(-1, 1)
y = df['jumlah cacat'].values.reshape(-1, 1)

x_train = x;
y_train = y;

lin_reg = LinearRegression()

lin_reg.fit(x_train, y_train)

var_coefficient = lin_reg.coef_
var_constant = lin_reg.intercept_

print("Constant (a): {0}".format(var_constant));
print("Coeficient (b): {0}".format(var_coefficient));

y_predicted = lin_reg.predict(x_train)
plt.scatter(x_train, y_train)
plt.plot(x_train, y_predicted, c='r')
plt.xlabel("rata-rata suhu ruangan")
plt.ylabel("jumlah cacat")
plt.title('"rata-rata suhu ruangan" vs "jumlah cacat"')

lin_reg.predict([[30]])
lin_reg.predict([[32]])
lin_reg.predict([[34]])


