num=list(map(int,input().split()))
num.sort(reverse=True)
print(int(str(num[0])+str(num[1]))+num[2])