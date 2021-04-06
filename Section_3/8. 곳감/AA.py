# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 07:10:05 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
f=sys.stdin
n=int(f.readline())#f.readline())

mat=[list(map(int,f.readline().split())) for _ in range(n)]
#print(mat)
    
m=int(f.readline())

#rot=[]

for i in range(m):
    row, lr, k=map(int,f.readline().split())
    row, k= row-1, k%n
    #print(row, lr, k)
    if lr==1:   
        mat[row]=mat[row][-k:]+mat[row][:-k]
    else:
        mat[row]=mat[row][k:]+mat[row][:k]
#print(mat)

s, e= 0, n
tot=0
for i in range(n):
    tot+=sum(mat[i][s:e])
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(tot)
    

'''
for i in range(m):
    rot=list(map(int,f.readline().split()))
    
    move=rot[2]%n
    if rot[1]==0:   move=n-move
    ##print('n: %d, move: %d' %(n, move))
    r=rot[0]-1
    ##print(mat[r][:move],mat[r][move:])
    ##print(mat[r][-move:],mat[r][:-move])
    mat[r][:move],mat[r][move:]=mat[r][-move:],mat[r][:-move]

res=0
for i in range(n//2):
    res+=sum(mat[i][i:5-i])
for i in range(n//2+1):
    res+=sum(mat[n//2+i][n//2-i:n//2+i+1])
##print(mat)
#print(res)
    #rot.append(l)
'''