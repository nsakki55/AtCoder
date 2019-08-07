n,k=[int(input()) for _ in range(2)]

ans=1
t=[]

for i in range(n+1):
    t.append(2**i+k*(n-i))
    ans=1

print(min(t))