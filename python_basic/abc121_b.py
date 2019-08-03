n,m,c=map(int,input().split())
b=list(map(int,input().split()))

right=0

for i in range(n):
    a=list(map(int,input().split()))
    sum=0
    for j in range(m):
        sum+=a[j]*b[j]
    sum+=c
    if sum>0:
        right+=1

print(right)