# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:31:59 2020

@author: LMJ

"""
'''
readlines()로 index 붙이
with open('input.txt') as f:
    file=f.readlines()

n=int(file[0])
arr=[list(map(int, file[i].split())) for i in range(1, n+1)]
'''

import sys

f=open('input.txt','r')
#f=sys.stdin
n=int(f.readline())
l=list(map(int,f.readline().split()))

#print(n,l)
avg=round(sum(l)/len(l))

diff=float('inf')
loc=0

for i in range(len(l)):
    if abs(l[i]-avg)<diff:
        diff=abs(l[i]-avg)
        loc=i
    elif abs(l[i]-avg)==diff:
        if l[i]>l[loc]:
            diff=abs(l[i]-avg)
            loc=i
    #print(i, l[i], loc, l[loc])
            
            

print(avg, loc+1)
        
        
