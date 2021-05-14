# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:04:04 2020

@author: LMJ
"""

import sys

f=open('in2.txt', 'r')
f=sys.stdin

s=f.readline().strip()
d={'+':'(', '-':'(', '*':'+-(', '/':'+-(', '(':'+-*/', ')':'+-*/'}
#print(s)

res=''
op=[]
for x in s:
    if x.isdigit():
        res+=x
    else:
        if not op:
            op.append(x)
        else:
            if x==')':
                while op[-1]!='(':
                    res+=op.pop()
                op.pop()
            elif op[-1] in d[x]:
                op.append(x)    
            else:
                while op[-1] not in d[x]:
                    res+=op.pop()
                    if not op:  break
                op.append(x)
while op:
    res+=op.pop()
print(res)