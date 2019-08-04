a,b,c=map(int,input().split())
print(a if [a,b,c].count(a)==1 else b if [a,b,c].count(b)==1 else c)