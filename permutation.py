# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:28:13 2022

@author: Ogi Wemy
"""

from itertools import permutations

n = ['J', 'A', 'Y', 'A', 'P', 'U', 'R', 'A']

r_obj_observed = 3

seq = permutations(n, r_obj_observed)

lst_events = list(seq);

for p in lst_events:
    print(p)
    
    
print("\nMax probability event: {0}".format(len(lst_events)))