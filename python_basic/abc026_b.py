import numpy as np
n=int(input())
r=sorted([int(input())**2 for _ in range(n)],reverse=True)

print((sum(r[::2])-sum(r[1::2]))*np.pi)