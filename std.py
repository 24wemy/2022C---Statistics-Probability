# -*- coding: utf-8 -*-
"""
    Created on Tue Oct 18 20:24:12 2022
    @author: Ogi Wemy
    @desc :Create Normal Distribution from data
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def get_average(lst):
    return sum(lst) / len(lst)

def get_std(lst):
    mean = sum(lst) / len(lst)
    variance = sum([((x - mean) ** 2) for x in lst]) / len(lst)
    std = variance ** 0.5
    return std;

midterm_score = [70, 2, 68, 50, 90, 60, 79, 77, 190, 70, 89, 55, 75, 80, 96]

var_mean = get_average(midterm_score);
var_std = get_std(midterm_score);

print("Average: {0}".format(var_mean));
print("Standard Deviation: {0}".format(var_std));




