# -*- coding: utf-8 -*-

# Author : Corinta, Ogi Wemy
# Desc : Coefficient of variation (CV)


import numpy as np
from scipy import stats


x1 = [44, 50, 38, 96, 42, 47, 40, 39, 46, 50]


get_sample_std = np.std(x1, ddof=1)
get_population_std = np.std(x1)
get_sample_mean = np.sum(x1) / (len(x1) -1)
get_population_mean = np.sum(x1) / (len(x1))


get_cv = (get_sample_std * 100) / get_population_mean;

print("Sample of mean of data = ", get_population_mean)
print("Coefficient of variation : {0} ".format(get_cv))
