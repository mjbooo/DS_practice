# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:58:25 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
#f=sys.stdin



n, m=map(int,f.readline().split())
l=list(map(int,f.readline().split()))

l.sort()
lt, rt= 0, n-1

while lt<=rt:
    mid=(lt+rt)//2
    if l[mid]<m:    lt=mid+1
    elif l[mid]>m:  rt=mid-1
    else: 
        print(mid+1)
        break


'''
order=1

for x in l:
    if x<m:
        order+=1

print(order)
'''