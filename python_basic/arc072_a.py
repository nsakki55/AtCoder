n=int(input())
a=list(map(int,input().split()))

ans=0
b=[]
if a[0]==0:
    if a[1]>0:
        b.append(-1)
    else:
        b.append(1)
    ans+=1
else:
    b.append(a[0])

for i in range(1,n):
    if sum(b)>0 and sum(b)+a[i]<0:
        b.append(a[i])
    elif sum(b)<0 and sum(b)+a[i]>0:
        b.append(a[i])
    
    elif sum(b)>0 and sum(b)+a[i]>=0:
        b.append(a[i]-(sum(b)+a[i])-1)
        ans+=abs(-(sum(b)+a[i])-1)
        print(ans)

    elif sum(b)<0 and sum(b)+a[i]<=0:
        b.append(a[i]+abs(sum(b)+a[i])+1)
        ans+=abs((sum(b)+a[i])+1)
        print(ans)
    print(b)
print(ans)