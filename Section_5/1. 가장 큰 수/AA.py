# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:50:43 2020

@author: LMJ
"""

import sys

f=open('input.txt', 'r')
f=sys.stdin

n, m= map(int, f.readline().split())
l=[int(x) for x in str(n)]

#print(n ,m, l)

res=0
while l:
    idx=l.index(max(l[:m+1]))
    #print('l[:{}]: {}, max:{}'.format(m+1, l[:m+1], max(l[:m])))
    #print('l:{}, idx:{}, m:{}'.format(l, idx, m))
    m-=idx
    if len(l)==m:
        break;
    res=res*10+l[idx]
    l=l[idx+1:]
    #print(res)
print(res)