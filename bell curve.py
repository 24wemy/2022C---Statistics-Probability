# -*- coding: utf-8 -*-
"""
    Created on Tue Oct 18 20:33:47 2022
    @author: Ogi Wemy
    @desc : Create Normal Distributor from data
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

z_scores = [((stu_score-var_mean)/var_mean) for stu_score in midterm_score]

print("Average: {0}".format(var_mean));
print("Standard Deviation: {0}".format(var_std));

snd = stats.norm(var_mean, var_std)

plt.figure(figsize=(7.5,7.5))
plt.plot(midterm_score, snd.pdf(midterm_score))

plt.title('Normal Distribution (Student Midterm Scores)' ,fontsize= '15')
plt.xlabel('Z Scores', fontsize='15')
plt.ylabel('Probability Density' ,fontsize='15')
plt.show()

