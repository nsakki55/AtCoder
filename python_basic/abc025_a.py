s=list(input())
n=int(input())

total=[]
for i in range(len(s)):
    for j in range(len(s)):
        total.append(s[i]+s[j])

print(sorted(total)[n-1])