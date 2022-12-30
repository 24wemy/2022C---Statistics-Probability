# -*- coding: utf-8 -*-

# Author : Corinta, Ogi Wemy
# Desc : Sample and Population of Standard Deviation


import numpy as np
from scipy import stats


x1 = [44, 50, 38, 96, 42, 47, 40, 39, 46, 50]


get_sample_std = np.std(x1, ddof=1)
get_population_std = np.std(x1)
get_sample_mean2 = np.sum(x1) / (len(x1) -1)
get_population_mean2 = np.sum(x1) / (len(x1))


print("Input x: ", x1)
print("Sample Standard Deviation of x : ", get_sample_std)
print("Population Standard Deviation of x : {0} ".format(get_population_std))

