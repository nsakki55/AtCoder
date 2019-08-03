n,m=map(int,input().split())

common=[]

for i in range(n):
    k,*a=list(map(int,input().split()))
    common.extend(a)
print(len([num for num in set(common) if common.count(num)==n] ))