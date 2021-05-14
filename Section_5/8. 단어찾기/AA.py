# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:50:04 2020

@author: LMJ
"""

import sys

f=open('in5.txt', 'r')
f=sys.stdin

n=int(f.readline())
l= [f.readline().strip() for i in range(n)]
#print(l)
l=set(l)
for _ in range(n-1):
    x=f.readline().strip()
    #print(x, l)
    if x in l: l.remove(x)
print(l.pop())