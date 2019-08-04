y=int(input())

if y%400 == 0:
    print('YES')

else:
    if y % 100 ==0:
        print('NO')
    else:
        if y % 4 ==0:
            print('YES')
        else:
            print('NO')