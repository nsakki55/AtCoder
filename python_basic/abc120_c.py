s=list(input())

ans=[s[0]]
for i in range(1,len(s)):
    if len(ans) !=0 and ans[-1]!=s[i]:
        ans.pop(-1)
        continue
    
    else:
        ans.append(s[i])

print(len(s)-len(ans))