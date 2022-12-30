# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:43:17 2022

@author: Ogi Wemy
"""

from itertools import combinations

#define variables 
pejabat1 = 'Damri A'
pejabat2 = 'Damri B'
pejabat3 = 'DAmri C'
pejabat4 = 'Damri D'
pejabat5 = 'DAmri E'
pejabat6 = 'DAmri F'

n_pejabat = [pejabat1, pejabat2, pejabat3, pejabat4, pejabat5, pejabat6]
r_obj_observed = 4


#Library function 
seq = combinations(n_pejabat, r_obj_observed)

#get list events
lst_events = list(seq);

#show list 
for  event in lst_events:
  print(event)

#gel all probability events 
print("\nMax probability event:{0}".format(len(lst_events)))