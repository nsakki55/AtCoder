n = int(input())

p = list(map(int, input().split(' ')))

ans = 0
for i in range(n):
    flag = True

    if i > 0:

        if min(p[:i+1]) != p[i]:
            flag = False

    if flag:
        ans += 1

print(ans)
