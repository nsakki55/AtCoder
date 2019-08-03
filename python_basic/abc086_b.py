a,b=input().split()
n=int(a+b)
flag=True
for i in range(1000):
    if flag:
        if i**2==n:
            flag=False
            print('Yes')

if flag:
    print('No')