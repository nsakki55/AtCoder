n=int(input())
s=[str(input()) for _ in range(n)]
m=int(input())
t=[str(input()) for _ in range(m)]

l=set(s)
num=max(s.count(i)-t.count(i) for i in l)
print(max(0,num))
