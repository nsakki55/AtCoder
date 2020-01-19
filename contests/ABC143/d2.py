from scipy.special import comb
n=int(input())
l=list(map(int,input().split(' ')))

ans=0
l=sorted(l,reverse=True)

for i in range(0,n-2):
    for j in range(n-1,2,-1):
        if i<j-1:
            if l[i]<l[j]+l[j-1]:

                ans+=comb(n-j,2)
                    
print(ans)
