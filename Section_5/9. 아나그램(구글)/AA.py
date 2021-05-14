# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:01:53 2020

@author: LMJ
"""

import sys

f=open('input.txt', 'r')
f=sys.stdin

s1, s2=f.readline().strip(), f.readline().strip()
#print(s1, s2)
n=len(s1)
d1, d2={}, {}
for i in range(n):
    x1, x2= s1[i], s2[i]
    #print(x1, x2)
    if x1 in d1:
        d1[x1]+=1
    else:
        d1[x1]=1
        
    if x2 in d2:
        d2[x2]+=1
    else:
        d2[x2]=1
        
#print(d1, d2)
if d1==d2:
    print('YES')
else:
    print('NO')