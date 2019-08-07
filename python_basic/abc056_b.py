w,a,b=map(int,input().split())

if a<=b:
    print(max(b-a-w,0))
else:
    print(max(a-b-w,0))