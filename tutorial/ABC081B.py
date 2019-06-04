n=0
while n<1 or n>201:
    n=int(input())

map_lsit=map(int,input().split())
numbers=list(map_lsit)

step=0
check=0
while check==0:
    for i in range(0,n-1):
        if numbers[i]%2!=0:
            check+=1
            break
        else:
            numbers[i]=numbers[i]/2
    step+=1

print(step-1)
