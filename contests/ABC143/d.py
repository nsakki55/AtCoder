import itertools
n=int(input())
l=list(map(int,input().split(' ')))


ans=0
for com in list(itertools.combinations(l,3)):
    com=sorted(com)
    if com[2]<com[0]+com[1]:
        ans+=1

print(ans)