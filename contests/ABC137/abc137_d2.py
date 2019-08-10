n,m=map(int,input().split())

baito=[list(map(int,input().split())) for _ in range(n)]

baito=[k for k in baito if k[0]<=m]
baito.sort(key=lambda x:(x[1],x[0]))
baito=baito[::-1][:m]
ans=0
for i in baito:
    ans+=i[1]
print(ans)
#baito=[k for k in baito if k[0]+i<=m]