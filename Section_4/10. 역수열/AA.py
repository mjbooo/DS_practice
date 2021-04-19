# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:31:33 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
f=sys.stdin

n=int(f.readline())
r=list(map(int,f.readline().split()))


l, blank=[0]*n, list(range(n))
#print(blank)
for i in range(n):
    idx=blank.index(r[i])
    #print(i+1, r[i], idx)
    while l[idx]!=0:
        idx+=1
    l[idx]=i+1
    #print('changing blacnk:', -(n-idx)+1, ':')
    if -(n-idx-1)<0:
        blank[-(n-idx-1):]=map(lambda x: x-1, blank[-(n-idx-1):])
    #print('blank:',blank)
    #print('l',l,'\n')
    
 
for x in l:
    print(x, end=' ')
