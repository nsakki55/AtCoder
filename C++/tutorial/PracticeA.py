# -*- coding: utf-8 -*-
#input関数で入力を受け取る
a=int(input())
#split()で複数の分割を分ける。map()で第一引数の関数を第二引数に適応する。
b,c=map(int,input().split())
str=input()
#print(a)
#print(b,c)

print("{0} {1}".format(a+b+c,str))