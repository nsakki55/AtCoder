n=int(input())
a=list(map(int,input().split()))

a.insert(0,0)
a.append(0)

for i in range(1,n+1):
    ans=0
    tmp=a.copy()
    tmp.pop(i)
    for j in range(1,n+1):
        ans+=abs(tmp[j]-tmp[j-1])
    print(ans)