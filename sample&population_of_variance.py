# -*- coding: utf-8 -*-

# Author : Corinta, Ogi Wemy
# Desc : Sample and Population of Variance


import numpy as np
from scipy import stats

x1 = [44, 50, 38, 96, 42, 47, 40, 39, 46, 50]


get_sample_var = np.var(x1) / (len(x1) -1)
get_population_var = np.var(x1)

print("Input x: ", x1)
print("Sample variance of x : ", get_sample_var)
print("Population variance of x : {0} ".format(get_population_var))