n=int(input())
s=list(map(str,input().split()))
total=[]
for i in range(n):
    if s[i] not in total:
        total.append(s[i])
print('Three' if len(total)==3 else 'Four')