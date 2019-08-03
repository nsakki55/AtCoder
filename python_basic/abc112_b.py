N,T=map(int,input().split())

root=[]

for i in range(N):
    c,t=map(int,input().split())
    if t<=T: root.append(c)

print(min(root) if len(root)>0 else 'TLE')