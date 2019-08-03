n=int(input())

res=n

for i in range(n+1):
    cc=0
    while i>0:
        cc+=i%6
        i/=6
    t=n-i
    while t>0:
        cc+=t%9
        t/=9
    res=min(res,cc)
print(res)