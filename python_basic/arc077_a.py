n=int(input())
a_all=list(map(int,input().split()))
b=[]

for a in a_all:
    b.append(a)
    b=b[::-1]
print(b)