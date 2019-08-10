n,m=map(int,input().split())

a=[]
for _ in range(n):
    a.append(input())

b=[]
for _ in range(m):
    b.append(input())

flag=False
for i in range(n-m+1):
    if not flag:
        check=[]
        for j in range(m):
            if b[j] in a[i+j]:
                check.append(1)
        if sum(check)==m:
            flag=True

print('Yes' if flag else 'No')