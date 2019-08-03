n,m,x=map(int,input().split())
a=list(map(int,input().split()))

cost_right=0
cost_left=0

for i in range(x,n):
    if i in a:
        cost_right+=1

for j in range(0,x):
    if j in a:
        cost_left+=1

print(min(cost_right,cost_left))
