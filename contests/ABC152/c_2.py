n = int(input())

p = list(map(int, input().split(' ')))


ans = 1
min_num = p[0]

for i in range(n-1):
    if p[i+1] < min_num:
        ans += 1
        min_num = p[i+1]

print(ans)