# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:21:16 2020

@author: LMJ
"""

import sys

f=open('input.txt','r')
#f=sys.stdin

n=int(f.readline())
for i in range(n):
    '''
    if i!=n-1:
        l.append(f.readline()[:-1])
    else:
        l.append(f.readline())
    '''
    s=(f.readline().rstrip('\n'))
    if s==s[::-1]:
        print('#%d YES' %(i+1))
    else:
        print('#%d NO' %(i+1))
    #개행문자 없애기
#print(n)
#print(l)
'''
def tf2yn(n):
    if n==1:    return 'YES'
    else:   return 'NO'

l_yn=list(map(lambda x: tf2yn(x.lower()==x.lower()[::-1]), l))
#print(list(l_yn))

for i in range(n):
    print('#%d %s'%(i+1,l_yn[i]))
 '''         
'''
7
stts
moon
abcba
yes
goodboy
stttttts
tttttttttttttt

#1 YES
#2 NO
#3 YES
#4 NO
#5 NO
#6 YES
#7 YES
'''