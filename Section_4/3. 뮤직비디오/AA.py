# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:46:41 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
#f=sys.stdin

n, m= map(int, f.readline().split())
l=list(map(int, f.readline().split()))

lt, rt=1, sum(l) # range of length

res=sum(l)

while lt<=rt:
    mid=(lt+rt)//2
    local_sum=0
    cnt=1
    contain=True
    for x in l:
        local_sum+=x
        
        
        if x>mid:
            contain=False
            break
           
        if local_sum>mid:   
            cnt+=1
            local_sum=x
            
        '''
        if mid<=x:
            local_sum+=x
            if local_sum>mid:       
                cnt+=1
                local_sum=x
        else:
            contain=False
            break  
        '''
        if cnt>m:   
            contain=False
            ##print('overcount')
            #break
    print('cnt: %d, m: %d, lt: %d, rt: %d, mid: %d, contain: %s' %(cnt, m, lt, rt, mid, contain))
    
    if contain==False:
        lt=mid+1
    else:
        res=mid
        rt=mid-1
        
print(res)
    
    




'''
#failure1

tot=sum(l)
res=tot
sum_1= 0
for i in range(1,n-2):
    sum_1+=l[i-1]
    sum_2=0
    if sum_1>res:   break
    for j in range(i+1, n-1):
        sum_2+=l[j-1]
        if sum_2>res:   break
        sum_3=tot-(sum_1+sum_2)
        if sum_3>res:   continue
        sum_max=max(sum_1, sum_2, sum_3)
        if res> sum_max:
            res=sum_max
        #print('sum1: %d, sum2: %d, sum3: %d, res: %d' %(sum_1, sum_2, sum_3, res))
            
#print(res)
'''