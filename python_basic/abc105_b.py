n=int(input())

l=[4*x+7*y for x in range(26) for y in range(16)].count(n)
print('Yes' if l!=0 else 'No')