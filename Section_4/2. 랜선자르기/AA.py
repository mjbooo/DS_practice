# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:31:55 2020

@author: LMJ
"""

import sys

f=open('in2.txt','r')
f=sys.stdin

k, n= map(int,f.readline().split())

l=[int(f.readline()) for _ in range(k)]
#print(l)

#print(sum(l)//n)

lt, rt= 1, sum(l)//n
mid= (lt+rt)//2
while lt<=rt:
    tot=sum(map(lambda x: x//mid, l))
    #print('lt: %d, rt: %d, mid: %d, tot: %d, n: %d' % (lt, rt, mid, tot, n))
    
    '''
    if lt+1==rt:
        if sum(map(lambda x: x//rt, l))>=n:
            print(rt)
        else:
            print(lt)
        break
    if lt==rt:
        print(lt)
    '''
        
    if tot >= n:
        lt=mid+1
        res=mid
        mid=(lt+rt)//2
    else :
        rt=mid-1
        mid=(lt+rt)//2

print(res)
#print(mid, sum(map(lambda x: x//mid, l)))

'''
if lt==rt:
    print(mid)
    break;
'''
'''
    if mid==lt or mid == rt:
        break;
'''









'''
#m1

len_max=sum(l)//n
for len_tmp in range(len_max, 0, -1):
    l_cutted=map(lambda x: x//len_tmp, l)
    if sum(l_cutted)>=n:
        print(len_tmp)
        break
'''
