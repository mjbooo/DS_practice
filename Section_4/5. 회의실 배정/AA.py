# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 07:43:13 2020

@author: LMJ
"""

import sys

f= open('input.txt', 'r')
#f=sys.stdin

n=int(f.readline())
l=[list(map(int, f.readline().split())) for _ in range (n)]
sl, el= zip(*l)
#print(l)
#print(sl, el)
l.sort(key= lambda x: (x[1], x[0]))
#print(l)


cnt, end=0, 0
for s, e in l:
    if s>=end:
        end=e
        cnt+=1
print(cnt)
    



'''
cnt=0
end=0 #float('inf')

while True:
    loc_min=float('inf')
    for i in range(n):
        if sl[i]>=end and loc_min>el[i]:
            loc_min=el[i]
    if loc_min==float('inf'):
        break        
    end=loc_min
    cnt+=1
    #print(end)
    
            
print(cnt)
'''