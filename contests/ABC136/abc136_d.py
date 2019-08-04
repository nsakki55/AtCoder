#! /usr/bin/python
# -*- coding: utf-8 -*-

from numba import jit
s=list(input())

c=[1 for i in range(len(s))]
flag=True
his=[0,0]

def change(a,b):
    for i in range(len(s)):
        if s[i]=='R':
            b[i+1]+=a[i]
        else:
            b[i-1]+=a[i]
    return b

for k in range(1000000):

    his[1]=his[0]
    his[0]=c
    tmp=[0 for _ in range(len(s))]

    tmp=change(c,tmp)
    c=tmp
    #print(c)
    if c==his[0] or c==his[1] and k>2:
        break
if k%2!=1:
    print(' '.join(map(str,his[0])))    

else:
    print(' '.join(map(str,c)))