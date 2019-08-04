n = int(input())
s=[int(input()) for _ in range(n)]

print(sorted(list(set(s)),reverse=True)[1])