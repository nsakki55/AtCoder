a,b,k=map(int,input().split())

ans=list(set(list(i for i in range(a,a+k,1) if i<=b)+list(j for j in range(b,b-k,-1) if j>=a)))

for l in sorted(ans):
    print(l)
