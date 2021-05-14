# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:33:16 2020

@author: LMJ
"""

import sys 

f=open('in2.txt', 'r')
f=sys.stdin

s=f.readline().strip()
n=int(f.readline())

#l=[f.readline() for _ in range(n)]

for i in range(n):
    plan=f.readline()
    idx=0
    for x in plan:
        if x in s[idx:]:
            if x==s[idx]:
                idx+=1
            else:
                print('#{} NO'.format(i+1))
                break
    else:
        if idx==len(s)-1: 
            print('#{} NO'.format(i+1))
        else: 
            print('#{} YES'.format(i+1))

        