# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:51:42 2020

@author: LMJ
"""

import sys
#sys.stdin=open('input.txt','rt')

n, k=map(int, input().split())
#n,k=6,5
cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
        if cnt == k:   
            print(i)
            break
else:   print(-1)