n=int(input())
list=list(map(int,input().split()))

alice=[]
bob=[]

i=0
while len(list)>0:
    alice.append(max(list))
    list.remove(max(list))
    if len(list)>0:
        bob.append(max(list))
        list.remove(max(list))

print(sum(alice)-sum(bob))

