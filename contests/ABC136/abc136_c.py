n=int(input())
h=list(map(int,input().split()))

a=h[0]
flag=True
if h[0]>0:
    h[0]-=1

for i in range(1,n):
    if flag:
        if h[i]>0 and h[i]>h[i-1]:
            h[i]-=1
        
        elif h[i]>=0 and h[i]==h[i-1]:
            continue
        
        else:
            flag=False

if flag:
    print('Yes')
else:
    print('No')