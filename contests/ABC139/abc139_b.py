a,b=map(int,input().split())

ans=1
n=a
while n<b:
    n+=a-1
    ans+=1
if b==1:
    print(0)
else:
    print(ans)