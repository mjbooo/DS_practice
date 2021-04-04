# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:54:49 2020

@author: LMJ
"""


import sys

f=open('input.txt','r')
#f=sys.stdin

n_list=[]
l_list=[]

for i in range(2):
    n_list.append(int(f.readline()))
    l_list.append(list(map(int,f.readline().split())))

print(n_list, l_list)
print(l_list[0][0], l_list[1][0], sum(n_list))


res=[]
for i in range(sum(n_list)):
    print(i, res)
    if len(l_list[0])==0 or len(l_list[1])==0:
        l_last=l_list[0]*(len(l_list[0])!=0)+l_list[1]*(len(l_list[1])!=0)
        res+=l_last
        #print(l_last)
        break
    else:
        if l_list[0][0]>=l_list[1][0]:
            res.append(l_list[1].pop(0))    
        else:
            res.append(l_list[0].pop(0))
        
        
print(res)