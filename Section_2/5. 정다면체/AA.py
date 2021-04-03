# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:07:38 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
f=sys.stdin
#print(f.readline())
n, m=map(int,f.readline().split())



'''
#method1
n, m=min(n,m), max(n ,m)

if n==m:
    print(n+1)
else:
    for i in range(n+1,m+2):
        print(i, end=' ')
        
'''
    
#method2
cnt=[0]*(n+m+3)
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1

cnt_max=max(cnt)
for i in range(n+m+3):
    if cnt[i]==cnt_max:
        print(i, end=' ')