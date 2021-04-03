# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:07:38 2020

@author: LMJ
"""

import sys

f=sys.stdin
#f=open('input.txt','r')


n=int(f.readline())
#n=2
#print(n)
#n=5
l=[0]*(n+1)
cnt=0

for i in range(2, n+1):
    if l[i]==0: 
        cnt+=1
        for j in range(i,n+1,i):
            l[j]=1
print(cnt)

#prime_list= [l[i] for x in l if x!=0]

'''

def seive(l,x):
    tmp=list(enumerate(map(lambda y: y%x, l)))
    #print(tmp)
    l= [l[i] for i, j in tmp if j!=0]
    return l


l=list(range(3,n+1,2))
prime_list=[2]
for i in range(3, n+1, 2):
    if l[0]!=prime_list[len(prime_list)-1]: prime_list.append(l[0])
    l=seive(l,i)
    #print(i, l)
#print(l)
#print(prime_list)
print(len(prime_list))
'''



    

'''리스트 discrete 참조..?'''
'''
prime_cnt=0
for i in range(3,n+1,2):
    for prime in prime_list:  
        if i%prime==0:  break;
    else: prime_list.append(i)
    
#print(prime_list,prime_cnt)
#print((prime_list))
print(len(prime_list))
'''


'''

n=int(f.readline())
#print(n)
prime_list=[]
prime_cnt=0
for i in range(3,n+1,2):
    if len(prime_list)==0:  prime_list.append(2)
    
    for j in range(2,i//2+1):
        if i%j==0:  break
    else:  prime_list.append(i)
    #prime_cnt+=1;
    
    for prime in prime_list:
        
        if i%prime==0:  break;
    else: prime_list.append(i)
    
#print(prime_list,prime_cnt)
#print((prime_list))
print(len(prime_list))

'''