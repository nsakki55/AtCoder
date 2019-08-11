import math
a=list(map(int,input().split()))
a.sort()
b=a[2]-a[0]
c=a[2]-a[1]
b-=c
if b%2!=0:
	k=1
else:
	k=0
print(c+math.ceil(b/2)+k)
 