n,q=map(int,input().split())
N=[0 for _ in range(n)]

for i in range(q):
    l,r,t=map(int,input().split())
    for k in range(l,r+1):
        N[k-1]=t

for i in range(n):
    print(N[i])