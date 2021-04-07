# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:27:14 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
f=sys.stdin

#7*7 matrix
mat=[]
for i in range(7):
    mat.append(list(map(int,f.readline().split())))
#print(mat)

cnt=0
for i in range(7):
    for j in range(3):
        if mat[i][j:j+5]==mat[i][j:j+5][::-1]:
            cnt+=1
        #print(mat[i][j:j+5])

mat=[list(x) for x in zip(*mat)]
#print(mat)
for i in range(7):
    for j in range(3):
        if mat[i][j:j+5]==mat[i][j:j+5][::-1]:
            cnt+=1
print(cnt)