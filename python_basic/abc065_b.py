n=int(input())
s=list(int(input()) for _ in range(n))

push=[0 for _ in range(n)]
index=0
cnt=1
flag=True

while flag:
    push[index]+=1
    if s[index]==2:
        print(cnt)
        flag=False
    else:
        if push.count(2)!=0:
            print(-1)
            flag=False
        else: 
            index=s[index]-1
            cnt+=1
