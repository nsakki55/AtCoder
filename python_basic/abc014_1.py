a,b=[int(input()) for _ in range(2)]

print(b - a%b if a%b !=0 else 0)
