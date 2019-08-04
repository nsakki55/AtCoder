n=input()

k=len(n)//2
l=len(n)%2

ans=0
for i in range(0,2*k,2):
    ans+=9*10**i
if l!=0:
    ans+=int(n)-10**(len(n)-1)+1
print(ans)