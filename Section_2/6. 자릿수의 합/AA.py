# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:07:38 2020

@author: LMJ
"""

import sys

#f=open('input.txt','r')
f=sys.stdin

n=int(f.readline())
l=list(map(int,f.readline().split()))

def digit_sum(x):
    res=0
    while x!=0:
        res+=x%10
        x=x//10
    return res

l_digit_sum=list(map(lambda x: digit_sum(x),l))
max_value=max(l_digit_sum)
'''이 부분 item-index 더 매끄럽게 다루는 법'''
print(l[l_digit_sum.index(max_value)])