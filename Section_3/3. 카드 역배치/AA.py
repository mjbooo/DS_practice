# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:58:24 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
#f=sys.stdin

card=list(range(1,21))

for i in range(10):
    ai, bi=map(int,f.readline().split())
    card[ai-1:bi]=card[ai-1:bi][::-1]
#print(l)


for i in range(10):
    
    '''
    else:
        card[:bi]=card[:bi][::-1]
        '''

for x in card:
    print(x, end=' ') 