n,m,a,b=map(int,input().split())

c=list(int(input()) for _ in range(m))

flag=True
for i in range(m):
    if flag:
        if n<=a:n+=b
    
        n-=c[i]
        if n<0:
            print(i+1)
            flag=False

if flag:
    print('complete')