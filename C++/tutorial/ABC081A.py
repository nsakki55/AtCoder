a=int(input())
list=[]
while a>0:
    list.append(a%10)
    a//=10

list.reverse()

print(sum(list))


