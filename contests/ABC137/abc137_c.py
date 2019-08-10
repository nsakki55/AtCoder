import collections
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


n=int(input())

S=[''.join(sorted(input())) for _ in range(n)]

c=collections.Counter(S)
ans=0
for i in c.values():
    if i==2:
        ans+=1
    elif i>2:
        ans+=cmb(i,2)
print(ans)