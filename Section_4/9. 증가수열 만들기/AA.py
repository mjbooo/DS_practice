# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:53:52 2020

@author: LMJ
"""


import sys
from collections import deque as d

f=open('in2.txt','r')
#f=sys.stdin

n=int(f.readline())
l=list(map(int, f.readline().split()))
l=d(l)
cnt=0
last=-float('inf')
lr=''
while l:
    
        
    if l[0]>l[-1]:
        if l[-1]>last:
            cnt+=1
            last=l[-1]
            lr+='R'
        l.pop()
    else:
        if len(l)==1:
            print(l[0])
        if l[0]>last:
            cnt+=1
            last=l[0]
            lr+='L'
        l.popleft()
            
print(cnt)
print(lr)
        