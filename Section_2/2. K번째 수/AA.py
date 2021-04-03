# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:05:21 2020

@author: LMJ
"""
'''
import sys
sys.stdin=open('input.txt','rt')
'''

'''
readlines()로 index 붙이
with open('input.txt') as f:
    file=f.readlines()

n=int(file[0])
arr=[list(map(int, file[i].split())) for i in range(1, n+1)]

'''

import sys
sys.stdin=open('input.txt','rt')
 
t=int(sys.stdin.readline())
for i in range(t):
    n, s, e, k= map(int, sys.stdin.readline().split())
    #print (t,n,s,e,k)
    l=list(map(int, sys.stdin.readline().split()))
    l=l[s-1:e]
    #print(l)
    l.sort()
    print('#',i+1,' ',l[k-1],sep='')
