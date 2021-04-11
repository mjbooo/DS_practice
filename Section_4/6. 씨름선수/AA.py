# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 08:08:33 2020

@author: LMJ
"""

import sys

f= open('input.txt', 'r')
f=sys.stdin

n=int(f.readline())
l=[list(map(int, f.readline().split())) for _ in range (n)]

l.sort(reverse=True)
#print(l)

w_max=-float('inf')
cnt=n
for h, w in l:
    if w>w_max:
        w_max=w
    if w_max>w:
        cnt-=1

print(cnt)