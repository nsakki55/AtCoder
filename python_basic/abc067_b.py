n,k=map(int,input().split())

l=list(map(int,input().split()))

l_max=sorted(l,reverse=True)[:k]
print(sum(l_max))