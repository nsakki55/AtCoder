s=int(input())

def even(n):
    return n/2

def odd(n):
    return 3*n+1

flag=True
num=[s]

i=1
while flag:
    if s%2 ==0:
        s=even(s)
        if s in num:
            print(i+1)
            flag=False
        else:
            num.append(s)
            i+=1
    else:
        s=odd(s)
        if s in num:
            print(i+1)
            flag=False
        else:
            num.append(s)
            i+=1
