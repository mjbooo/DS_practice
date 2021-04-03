# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:07:38 2020

@author: LMJ
"""

import sys

f=sys.stdin
f=open('input.txt','r')

n=int(f.readline())
ox=list(map(int,f.readline().split()))


'''
#method1
score=[0]*n


cont=0 #1 if got win in previous stage
for i in range(n):
    if ox[i]==0:    
        score[i]=0
    else:
        if i==0:
            score[0]=1
            continue
        score[i]=score[i-1]+1
        #cont=1

print(sum(score))
'''

cont=0
sum=0
for x in ox:
    if x==0:
        cont=0
    else:
        cont+=1
        sum+=cont

print(sum)
        