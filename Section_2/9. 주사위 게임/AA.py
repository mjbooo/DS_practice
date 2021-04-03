# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:53:24 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
f=sys.stdin

n=int(f.readline())
l=[]
for i in range(n):
    l.append(list(map(int,f.readline().split())))
#print(l)
    

def reward(l):
    if l[0]==l[1]==l[2]:
        return 10000+l[0]*1000
    elif l[0]==l[1] or l[0]==l[2]:
        return 1000+l[0]*100
    elif l[1]==l[2]:
        return 1000+l[1]*100
    else:
        return max(l)*100
        
l_reward=list(map(reward,l))
print(max(l_reward))