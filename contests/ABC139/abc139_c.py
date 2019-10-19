n=int(input())
h=list(map(int,input().split()))

ans=0
i=0

while i<n:
for l in range(n-i):
    if i+l<=n:
        tmp=0
        #print(i+l)
        if h[i+l]>=h[i+l+1]:
            tmp+=1
        else:
            i=i+l+1
            print(i)
            break
        ans=max(tmp,ans)
print(ans)