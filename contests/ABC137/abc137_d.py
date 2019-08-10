n,m=map(int,input().split())

baito=[list(map(int,input().split())) for _ in range(n)]

ans=0
for i in range(m):
    baito=[k for k in baito if k[0]+i<=m]
    baito.sort(key=lambda x:(x[0],x[1]))
    print(baito[::-1])
    if len(baito)!=0:
        ans+=baito[::-1][0][1]
        baito.remove(baito[::-1][0])
print(ans)