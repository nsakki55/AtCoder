n,m=map(int,input().split())

s=[i for i in range(1,n+1)]

for i in range(m):
    k=int(input())
    s.remove(k)
    s.insert(0,k)

for j in s:
    print(j)