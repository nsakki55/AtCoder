n=int(input())
S=[]
P=[]
for i in range(n):
  s,p=input().split()
  S.append(s)
  P.append(int(p))

total=sum(P)
city='atcoder'

for i in range(n):
    if P[i]>total/2:
        city=S[i]

print(city)