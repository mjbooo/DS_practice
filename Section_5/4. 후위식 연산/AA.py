# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 07:18:05 2020

@author: LMJ
"""

import sys

f=open('in2.txt', 'r')
f=sys.stdin

l= list(str(f.readline().strip()))
#l=list('35+2*')

stack=[]


for x in l:
    #print(x, stack, end=' to ')
    if x.isdigit():
        stack.append(x)        
    else:
        op2=stack.pop()
        '''
        print('x:', x)
        print('op2: ',op2)
        print('stack: ',stack)
        '''
        op1=stack.pop()
        
        res=eval(op1+x+op2)
        stack.append(str(res))
        
    #print(stack)

print(int(stack[-1]))
