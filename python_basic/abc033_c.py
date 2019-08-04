s=input().split('+')
ans=0
for i in range(len(s)):
    if '0' not in s[i]:
        ans+=1
print(ans)