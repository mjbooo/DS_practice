# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:32:42 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
f=sys.stdin


mat=[]
r0, r1, r2=[],[],[]
for i in range(9):
    row=list(map(int,f.readline().split()))
    mat.append(row)
    if i%3==0:
        r0+=row
    elif i%3==1:
        r1+=row
    else:
        r2+=row
    
#print(mat)
#print(mat)
e=set(range(1,10))
e_diag=[r0, r1, r2]
#print(e_diag)
#print(e_diag[0:1][0])
for i in range(9):
    cond_rc= (set(mat[i][:])==e and set(mat[:][i])==e)
    cond_diag= e==set(e_diag[0][3*i:3*i+3]+e_diag[1][3*i:3*i+3]+e_diag[2][3*i:3*i+3])
    #print(cond_rc, cond_diag)
    if not (cond_rc and cond_diag):
        print('NO')
        break
else:
    print('YES')    