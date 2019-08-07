n=int(input())
l=list(map(int,input().split()))

l_max=max(l)
res=sum(l)-l_max

print('Yes' if res>l_max else 'No')