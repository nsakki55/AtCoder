n=int(input())

s=list(input())

ans=0
t=[0]

for i in s:
    if i=='I':
        ans+=1
    else:
        ans-=1
    t.append(ans)

print(max(t))