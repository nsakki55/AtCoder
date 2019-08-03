n=int(input())

flag=True


for i in range(n):
    if 2**i>n:
        if flag:
            flag=False
            print(2**(i-1))
if n==1:
    print(1)