n=int(input())

a=[int(input()) for i in range(n)]

a=[i -min(a) for i in a]
print(a)