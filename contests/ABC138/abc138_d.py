import sys
sys.setrecursionlimit(10**6)
s=input()
t=input()

if not set(list(t))<=set(list(s)):
    print(-1)

else:
    ans=s*10**5
    t=list(t)

    i=0
    flag=True
    for l in range(len(ans)):
        if flag:
            if t[0] == ans[i]:
                del t[0]
            i+=1
            if len(t)==0:
                flag=False
    print(i)