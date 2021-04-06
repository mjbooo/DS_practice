# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:21:38 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
#f=sys.stdin

n=int(f.readline())

l=[[0 for _ in range(n+2)]]
for i in range(n):
    l.append([0]+list(map(int,f.readline().split()))+[0])
l.append([0 for _ in range(n+2)])

dx, dy= zip(*[(0,-1), (-1,0), (0,1), (1,0)])
cnt=0
for i in range(1,n+2):
    for j in range(1,n+2):
        #if l[i][j]>l[i-1][j] and l[i][j]>l[i][j-1] and l[i][j]>l[i+1][j] and l[i][j]>l[i][j+1]:
        if all (l[i][j]>l[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)            
    