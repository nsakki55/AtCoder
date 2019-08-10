n=int(input())

T=sorted([int(input()) for _ in range(n)])[::-1]

x=y=0

for t in T:
    if x<y:
        x+=t
    else:
        y+=t
    
print(max(x,y))
