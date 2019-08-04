s=input()

if s[0]=='A':
    if s[2:-1].count('C')==1:
        index=s[2:-1].index('C')
        print(index)
        tmp=s[1]+s[index+3:]
        print(tmp)
        if tmp==tmp.lower():
            print('hre')
            print('AC')
        else:
            print('WA')
    else:
        print('WA')
else:
    print('WA')

