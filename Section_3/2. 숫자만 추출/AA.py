# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:44:32 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
#f=sys.stdin

s=f.readline()
#print(s)
text=''

for c in s:
    '''
    isdigit 함수로 대체 
    
    if c in list(map(str,list(range(10)))):
        text+=c
    '''
    
    if c.isdigit():
        text+=c
n=int(text)

cnt=0
for i in range(1,n//2+1):
    if n%i==0:
        #print(cnt)
        cnt+=1
  
print(n)
print(cnt+1)
