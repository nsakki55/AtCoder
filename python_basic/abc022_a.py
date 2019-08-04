n,s,t=map(int,input().split())
w=int(input())
a=list(int(input()) for _ in range(n-1))

if s<=w and w<=t:
    cnt=1
else:
    cnt=0

for i in range(n-1):
    w+=a[i]
    if s<=w and w<=t:
        cnt+=1

print(cnt)