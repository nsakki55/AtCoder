n=int(input())
mochi_list=[]
for i in range(0,n):
    mochi_list.append(int(input()))

mochi_list=list(set(mochi_list))
mochi_list.sort(reverse=True)

print(len(mochi_list))