# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:32:12 2020

@author: LMJ
"""


import sys

f=open('in1.txt', 'r')
f=sys.stdin

s=f.readline().strip()

#print(s, type(s))


'''
s='(((()(()()))(())()))(()())'
print(s, type(s))
'''

cont, res= 0, 0

while s:
    if s[:2]=='()':
        res+=cont
        s=s[2:]
    elif s[0]=='(':
        cont+=1
        s=s[1:]
    elif s[0]==')':
        cont-=1
        res+=1
        s=s[1:]

print(res)
