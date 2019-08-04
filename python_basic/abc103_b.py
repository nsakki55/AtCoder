s=list(input())
t=list(input())

def shift(l,n):
    return l[n:]+l[:n]
flag=True
for i in range(len(s)):
    if flag:
        if s==t:
            flag=False
            print('Yes')
        
        else:
            t=shift(t,1)

if flag:
    print('No')