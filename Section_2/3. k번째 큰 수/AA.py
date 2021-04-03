# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:05:21 2020

@author: LMJ
"""

import sys
#sys.stdin=open('input.txt','rt')

n,K=map(int, sys.stdin.readline().split())
l=list(map(int, sys.stdin.readline().split()))
#print(n,k,l)
l_sum=[]
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            l_sum.append(l[i]+l[j]+l[k])

#print(l_sum)

res=[]
for x in l_sum:
    if x not in res: res.append(x)
res.sort(reverse=True)

#print(res)
print(res[K-1])

