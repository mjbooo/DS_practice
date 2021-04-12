# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:17:40 2020

@author: LMJ
"""


import sys

f= open('input.txt', 'r')
#f=sys.stdin

n=int(f.readline())
l=list(map(int, f.readline().split()))
m=int(f.readline())

l.sort()
#print(l)
for i in range(m):
    l[-1]-=1
    l[0]+=1
    l.sort()
print(l[-1]-l[0])