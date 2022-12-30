# -*- coding: utf-8 -*-
"""
    Created : Oct 17 15:44:57 2022
    @author: Ogi Wemy
    @desc  :
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

var_mean = 0
var_std = 1
snd = stats.norm(var_mean, var_std)


x = np.linspace(-5, 5, 100)

plt.figure(figsize=(7.5,7.5))
plt.plot(x, snd.pdf(x))
plt.xlim(-5, 5)
plt.title('Normal Distribution', fontsize='15')
plt.xlabel('Values of Random Variable X', fontsize='15')
plt.ylabel('Probability', fontsize='15')
plt.show()
