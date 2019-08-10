h,w=map(int,input().split())

a=[]

for i in range(h):
    a.append(input())

print('#'*(w+2))
for j in range(h):
    print('#'+a[j]+'#')
print('#'*(w+2))