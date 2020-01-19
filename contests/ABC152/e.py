from fractions import gcd
from functools import reduce

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


n = int(input())

a = list(map(int, input().split(' ')))

# 最大公倍数
target_num = lcm(*a)

ans = 0
for i in range(n):
    ans += target_num//a[i]
#b = [target_num//num for num in a]

print(ans % (10**9+7))
