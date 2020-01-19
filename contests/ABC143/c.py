n=int(input())
s=list(input())

flag=True

while flag:
    ans=[]
    for i in range(len(s)):
        if i==0:
            ans.append(s[i])
        else:
            if s[i-1]!=s[i]:
                ans.append(s[i])

    if ans==s:
        flag=False
    else:
        s=ans
print(len(ans))