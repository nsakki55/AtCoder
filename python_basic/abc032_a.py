import math
a,b,n=[int(input()) for _ in range(3)]

def lcm(x,y):
    return (x*y)//math.gcd(x,y)


num=lcm(a,b)

for i in range(1,1000):
    if num*i>=n:
        print(num*i)
        break