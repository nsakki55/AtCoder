k,s=map(int,input().split())

print(len([i for i in range(k+1)  for j in range(k+1)  for l in range(k+1) if i+j+l==s] ))