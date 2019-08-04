n=int(input())
c=list(input())

total=[]
for i in range(1,5):
    total.append(c.count(str(i)))

print(max(total),min(total))