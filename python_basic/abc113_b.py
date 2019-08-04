n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))

temp_abs=[]
for i in range(n):
    temp=t-h[i]*0.006
    temp_abs.append(abs(a-temp))
print(temp_abs.index(min(temp_abs))+1)