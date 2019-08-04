s=list(input())
n=list(map(int,input().split()))
for i in range(4):
    s.insert(n[i]+i,'"')
print(''.join(s))