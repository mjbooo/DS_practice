# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:23:24 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
f=sys.stdin

mat=[]
l_sum=[]

n=int(f.readline())
mat=[list(map(int,f.readline().split())) for _ in range(n)]
print(l)
'''
for i in range(n):
    l=list(map(int,f.readline().split()))
    #print(l)
    mat.append(l)
    l_sum.append(sum(l))
'''
#col

largest=-float('inf')
for i in range(n):
    sum_row, sum_col= 0, 0
    for j in range(n):
        sum_row+=mat[i][j]
        sum_col+=mat[j][i]
    if largest<max(sum_row, sum_col):
        largest=max(sum_row, sum_col)

#diagonal
for i in range(n):
    sum_diag1, sum_diag2= 0, 0
    sum_diag1+=mat[i][i]
    sum_diag2+=mat[i][n-1-i]
if largest<max(sum_diag1, sum_diag2):
    largest=max(sum_diag1, sum_diag2)

print(largest)
    
        
'''
for i in range(n):
    sum_col=0
    for j in range(n):
        sum_col+=mat[j][i]
    l_sum.append(sum_col)

tmp=0
for i in range(n):
    tmp+=mat[i][i]
l_sum.append(tmp)

tmp=0
for i in range(n):
    tmp+=mat[i][n-i-1]
l_sum.append(tmp)
    
print(max(l_sum))
'''