n=int(input())

num=1
flag=True
for i in range(n):
    if flag:
       if i**2>n:
            num=(i-1)**2
            flag=False
            break
print(num)