a,b,c=map(int,input().split())

flag=True
for i in range(a*b):
    if flag:
        if (a*i)%b==c:
            flag=False
            print('YES')
if flag:
    print('NO')