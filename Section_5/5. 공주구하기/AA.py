# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:21:58 2020

@author: LMJ
"""

import sys
f=open('input.txt', 'r')
f=sys.stdin
n, k= map(int, f.readline().split())
l=list(range(1,n+1))
#print(l)

while len(l)!=1:
    for i in range(k):
        if i==k-1:
            l.pop(0)
            break
        l.append(l.pop(0))

print(l[0])
            
        