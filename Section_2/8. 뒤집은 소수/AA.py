# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:07:38 2020

@author: LMJ
"""

import sys

f=sys.stdin
#f=open('input.txt','r')

n=int(f.readline())
l=list(map(int,f.readline().split()))

'''
testcase2
l=[469,84 ,8851, 189, 69 ,1210, 682, 57 ,6217, 484, 8 ,3590, 662, 36 ,8275, 887 ,17 ,1254, 462, 67, 8969, 141, 70, 5603, 958, 100 ,3843]
'''
def isPrime(x):
    if x==1: return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    else:
        return True

def reverse(x):
    return int(str(x)[::-1])

l_reverse=list(map(reverse,l))
for x in l_reverse:
    if isPrime(x)==True:
        print(x, end=' ')

'''
27
469 84 8851 189 69 1210 682 57 6217 484 8 3590 662 36 8275 887 17 1254 462 67 8969 141 70 5603 958 100 3843 

953 71 7 859
'''