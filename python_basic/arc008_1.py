n=int(input())
k=n//10
print(k*100+15*(n-k*10) if k*100+15*(n-k*10)<(k+1)*100 else (k+1)*100)