k,x=map(int,input().split())

print(' '.join(map(str,sorted(set([i for i in range(x-k+1,x+k)])))))