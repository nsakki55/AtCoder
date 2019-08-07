s=list(input())
odd=[]
for i in range(len(s)):
    if i%2==0:
        odd.append(s[i])
print(''.join(odd))