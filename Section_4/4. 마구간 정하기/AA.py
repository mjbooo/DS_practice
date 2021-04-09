# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:10:43 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
#f=sys.stdin

n, c= map(int, f.readline().split())
l=[int(f.readline()) for _ in range(n)]

l.sort()
d=[l[i+1]-l[i] for i in range(n-1)]


#print(d)
lt, rt=1, sum(d)
res=1


while(lt<=rt):
    mid=(lt+rt)//2 # max of minimum distance
    cnt=1
    
    local_sum=0
    cond=True
    #print('p1 cnt: %d, c: %d, lt: %d, rt: %d, mid: %d, cond: %s' %(cnt, c, lt, rt, mid, cond))
    for x in d:
        #print("local_sum: %d, x: %d, mid: %d, cnt: %d" %(local_sum, x, mid, cnt))
        local_sum+=x
        
        '''
        if x>mid:   #최대거리 mid 보다 큰 거리 있음
            cond=False
            break
        '''
        if local_sum >=mid:
            local_sum=0
            cnt+=1
    if cnt<c:
        cond=False
    #print('c: %d, lt: %d, rt: %d, mid: %d, cond: %s' %(c, lt, rt, mid, cond))
    if cond:
        res=max(res,mid)
        lt=mid+1
    else:
        rt=mid-1
        
print(res)
    