
n,m=map(int,input().split())

ans=[0]*n

total=[]

for i in range(m):
    c=sorted(list(map(int,input().split())))
    ans[c[0]-1]+=1
    ans[c[1]-1]+=1
    total.append(c)

print(*ans,sep='\n')