# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:39:01 2022

@author: Ogi Wemy
"""

from itertools import combinations
 
n = [1,2,3,4,5,6,7,8,9,10]
r_obj_observed = 4
 
seq = combinations(n,r_obj_observed)

lst_events = list(seq);

for event in lst_events:
  print(event)

print("\nMax probability event:{0}".format(len(lst_events)))