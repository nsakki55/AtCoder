n=int(input())
v=sorted(map(int,input().split()))

for i in range(n):
    if len(v)>1:
        mean=(v[0]+v[1])/2
        v=v[2:]
        v.append(mean)
        v.sort()

print(v[0])


