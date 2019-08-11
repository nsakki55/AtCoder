n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))

total=[]
for i in range(n):
    ans=0
    for j in range(n):
        if j<i:
            ans+=a1[j]
        elif j==i:
            ans+=a1[j]+a2[j]
        else:
            ans+=a2[j]
    total.append(ans)

print(max(total))