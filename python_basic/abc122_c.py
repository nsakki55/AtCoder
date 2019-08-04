n,q=map(int,input().split())
s=input()
ans=[]
for i in range(q):
    l,r=map(int,input().split())
    ans.append(s[l-1:r].count('AC'))
for i in range(len(ans)):
    print(ans[i])