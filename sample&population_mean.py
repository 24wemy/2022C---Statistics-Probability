# -*- coding: utf-8 -*-

# Author : Corinta, Ogi Wemy
# Desc : Sample & Population mean


import numpy as np 



x = [77, 50, 99, 60, 90, 82,
     93, 75, 86, 99, 55, 79]

get_sample_mean = np.sum(x) / (len(x) -1)
get_population_mean = np.sum(x) / (len(x))

print("Input : ", x)
print("Sample mean of x : ", get_sample_mean)
print("Population mean of x : ", get_population_mean)