n,a,b=map(int,input().split())
# 各桁をばらす関数
def list_convet(num):
    list = []
    while num>0:
        list.append(num%10)
        num//=10
    list.reverse()
    return list

numbers=[]
for i in range(1,n+1):
    summary=sum(list_convet(i))
    if summary>=a and summary <=b:
        numbers.append(i)

print(sum(numbers))


