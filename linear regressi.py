# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:18:08 2022

@author: Ogi Wemy
"""


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sklearn.metrics as sm
import numpy as np

# Step#2 - read dataset (training & testing data)
path = "D:/exercise/";
df_train = pd.read_csv(path+'train_automobile.csv', usecols=['horsepower', 'price'])
df_test = pd.read_csv(path+'test_automobile.csv', usecols=['horsepower', 'price'])

# Independent variabel (x) is horsepower.
# Dependent variabel (y) is price.

# view info total data, tipe data, memory usage, etc.
df_train.info()
df_test.info()

# Step#3 - Exploratory Data Analysis (EDA) to find new insights in data.
# univariate analysis (view distribusi in horsepower)
f = plt.figure(figsize=(12,4))
f.add_subplot(1,2,1)
df_train['horsepower'].plot(kind='kde')
f.add_subplot(1,2,2)
plt.boxplot(df_train['horsepower'])
plt.show()

# univariate analysis (view distribusi dari price)
f = plt.figure(figsize=(12,4))
f.add_subplot(1,2,1)
df_train['price'].plot(kind='kde', c='g')
f.add_subplot(1,2,2)
plt.boxplot(df_train['price'])
plt.show()

# bivariate analysis (horsepower and price using scatter plot)
plt.scatter(df_train['horsepower'], df_train['price'], color='red', marker='x')
plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.title('Scatter Plot Horsepower vs Price')
plt.show()

# Step#4 - Generate Model Simple Linear Regression
# 4a - create variabel x (input) and y (output)
# Training data
x_train = df_train['horsepower'].values.reshape(-1,1)
y_train = df_train['price'].values.reshape(-1,1)
# Testing data
x_test = df_test['horsepower'].values.reshape(-1,1)
y_test = df_test['price'].values.reshape(-1,1)

# 4b - create object of linear regresi
lin_reg = LinearRegression()

# 4c - training the model using training data
lin_reg.fit(x_train, y_train)

# 4d - find slope/koefisien (b) value and intercept (a) value
var_coefficient = lin_reg.coef_ # slope or coefficient or kemiringan
var_constant = lin_reg.intercept_ # constant or intercept or memotong

print("Constant (a): {0}".format(var_constant));
print("Coefficient Regression (b): {0}".format(var_coefficient));

# 4e - find accuracy score of model
lin_reg.score(x_test, y_test)

# Step#5 - visualize Regression Line using data testing.
y_pred = lin_reg.predict(x_test)
plt.scatter(x_test, y_test, color='red', marker='x')
plt.plot(x_test, y_pred, color='blue')  # draw line
plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.title('Scatter Plot Horsepower vs Price')

# Step#6 - predict the car price with horsepower 100, 150, and 200.
lin_reg.predict([[100]])
lin_reg.predict([[150]])
lin_reg.predict([[200]])

# Step#7 - model evaluation
print("Mean Absolute Error (MAE): ", round(sm.mean_absolute_error(y_test, y_pred), 2)) 
print("Mean Squared Error (MSE): ", round(sm.mean_squared_error(y_test, y_pred), 2)) 
print('Root Mean Squared Error (RMSE):', np.sqrt(sm.mean_squared_error(y_test, y_pred)))
print("R2 score:", round(sm.r2_score(y_test, y_pred), 2))

# (find errors) selisih antara nilai sebenarnya (actual price) dengan nilai prediksi (predicted price)
arr_error = np.subtract(y_test, y_pred);
df_error = pd.DataFrame({'Actual Price': y_test.flatten(), 'Predicted Price': y_pred.flatten(), 'error': arr_error.flatten()})
df_error['Predicted Price'] = np.round(df_error['Predicted Price'], decimals = 2) # Round Values
df_error['error'] = np.round(df_error['error'], decimals = 2) # Round Values
 
# visualize with bar graph
df1 = df_error.head(40) # select 25 rows
df1.plot(kind='bar',figsize=(16, 10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# =============================================================================
# Remove residual index 15, 16 and 28
# =============================================================================
# Drop a list of rows by index
df_test_rem = df_test.drop([15, 16, 28], axis=0, inplace=False)
x_test_rem = df_test_rem['horsepower'].values.reshape(-1,1)
y_test_rem = df_test_rem['price'].values.reshape(-1,1)

# predict
y_pred_rem = lin_reg.predict(x_test_rem)

# Model evaluation
print("Mean Absolute Error (MAE): ", round(sm.mean_absolute_error(y_test_rem, y_pred_rem), 2)) 
print("Mean Squared Error (MSE): ", round(sm.mean_squared_error(y_test_rem, y_pred_rem), 2)) 
print('Root Mean Squared Error (RMSE):', np.sqrt(sm.mean_squared_error(y_test_rem, y_pred_rem)))
print("R2 score:", round(sm.r2_score(y_test_rem, y_pred_rem), 2))

