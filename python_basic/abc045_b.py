a=list(input())
b=list(input())
c=list(input())

flag=True
turn='a'

while flag:
    if turn=='a':
        if len(a)==0:
            winner='A'
            flag=False
        else:
            turn=a.pop(0)

    if turn=='b':
        if len(b)==0:
            winner='B'
            flag=False
        else:
            turn=b.pop(0)

    if turn=='c':
            if len(c)==0:
                winner='C'
                flag=False
            else:
                turn=c.pop(0)

print(winner)