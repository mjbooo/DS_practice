# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 07:37:49 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
f=sys.stdin

n, m= map(int, f.readline().split())
l=list(map(int, f.readline().split()))

l.sort()
#print(m)

cnt=0
while l:
    if l[0]+l[-1]>m:
        l.pop()
        cnt+=1
    else:
        l.pop()
        l.pop(0)
        cnt+=1
        
    if len(l)==1:
        cnt+=1
        break
        

print(cnt)



'''
for i in range(n):
    m_sum+=m[i]
    n_sum+=1
    if m[i]>m_limit:
        cnt+=n-(i+1)
        break
    if m_sum>m_limit:
        cnt+=1
        m_sum=m[i]
        n_sum=1
    
    if n_sum>=2:
        cnt+=1
        m_sum=0
        n_sum=0
    '''
        
    
'''
    m_sum+=m[i]
    n_sum+=1
    if m_sum>m_limit or n_sum>2:
        m_sum=m[i]
        n=1
        cnt+=1
    if m[i]>m_limit:
        cnt+=n-(i+1)
        break
        '''

'''m_sum+=m[i]
    n_sum+=1
    if local_sum>m_limit:
        cnt+=1
        local_sum=m[i]
    if m[i]>m_limit:
        cnt+=n-(i+1)
        break
        '''
    
