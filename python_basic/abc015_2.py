import math
n=int(input())
a=list(map(int,input().split()))
num=n-a.count(0)
print(math.ceil(sum(a)/num))