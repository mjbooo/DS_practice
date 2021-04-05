# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 06:39:43 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
f=sys.stdin
n=int(f.readline())
mat=[list(map(int,f.readline().split())) for _ in range(n)]
#print(mat)

s, e= n//2, n//2+1
tot=0
for i in range(n):
    tot+=sum(mat[i][s:e])
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(tot)
        
    
    
    


'''    
#print(mat)
res=0
for i in range(n//2):
    res+=sum(mat[i][n//2-i:n//2+i+1])
    #print(mat[i][n//2-i:n//2+i+1])
#print(res)
for i in range(n//2+1):
    
    res+=sum(mat[n//2+i][i:n-i])
    #print(mat[n//2+i][i:n-i])
print(res)
'''
    