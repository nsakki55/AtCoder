import re
s=str(input())
s=re.split('[^ACGT]',s)

ans=0
for i in range(len(s)):
    ans=max(ans,len(s[i]))

print(ans)