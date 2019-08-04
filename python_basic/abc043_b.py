s=list(input())
ans=[]

for i in range(len(s)):
    if s[i]=='0' or s[i]=='1':
        ans.append(s[i])
    else:
        if len(ans)!=0:
            ans.pop(-1)
        else:
            continue
    
print(''.join(ans))