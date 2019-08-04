n=int(input())
a=list(map(int,input().split()))

cnt=0

def half(n):
    return n*(1/2)

for i in range(min(a)//2):
    
    tmp=list(filter(lambda x:x%2==0,a))
    if len(tmp)==len(a):
        a=list(map(half,a))
        cnt+=1
    else:
        break
print(cnt)