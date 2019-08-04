a,b,c=[int(input()) for _ in range(3)]
total=[a,b,c]

for i in range(3):
    print(sorted(total,reverse=True).index(total[i])+1)
