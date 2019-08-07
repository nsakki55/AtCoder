n=int(input())

ans=[]

for i in range(n):
    a=int(input())
    if a in ans:
        ans.remove(a)
    else:
        ans.append(a)


print(len(ans))