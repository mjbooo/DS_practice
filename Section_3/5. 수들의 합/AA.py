# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 08:26:07 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
f=sys.stdin


n, m= map(int,f.readline().split())
#n>=1
l=list(map(int,f.readline().split()))

#print(n,m,a)

cnt=0
#m3


lt, rt=0, 0

tmp=l[0]

while(True):
    #print('lt: %d, rt: %d, local_sum: %d'%(lt, rt,tmp))
    if tmp==m:
        tmp-=l[lt]
        lt+=1
        cnt+=1
    elif tmp<m:
        if rt==n-1:
            break
        tmp+=l[rt+1]
        rt+=1
    else:
        tmp-=l[lt]
        lt+=1
print(cnt)
        
            










'''
#m1
for i in range(n):
    local_sum=0
    for j in range(i,n):
        local_sum+=a[j]
        if local_sum>m:
            break
        elif local_sum==m:
            cnt+=1
            break         
'''
'''
local_sum=[0]*n
tmp=0
for i in range(n):
    tmp+=a[i]
    local_sum[i]=tmp

l=local_sum
#print(n)
for i in range(n):
    if i>=1:
        l=list(map(lambda x: x-a[i-1], l[1:]))
        #print(l)
    if m in l:
        #print(l)
        cnt+=1
#print(local_sum)
    
print(cnt)
'''