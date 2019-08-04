a=1
b=2
n=int(input())

for i in range(n-1):
    a,b=a+b,a
print(a)