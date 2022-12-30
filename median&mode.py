# -*- coding: utf-8 -*-

# Author : Corinta, Ogi Wemy
# Desc : Median and Mode


import numpy as np 
from scipy import stats


x1 = [77, 50, 99, 60, 90, 82,
     93, 75, 86, 99, 55, 79]


get_mode = stats.mode(x1)
get_median = np.median(x1)

print("Input x1: ", x1)
print("Mode of x1 : ", get_mode[0])
print("Median of x1 : {0} ". format(get_median))