n=int(input())
s=list(input())
ans=0
for i in range(len(s)):
    x=len(set(s[:i]) & set(s[i:]))
    if ans <x:
        ans=x
print(ans)