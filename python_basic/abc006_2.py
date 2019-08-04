n=int(input())
a=[0,0,1]

for i in range(n-2):
    a_new=sum(a)
    a[2]=a[1]
    a[1]=a[0]
    a[0]=a_new
print(a[0]%10007)