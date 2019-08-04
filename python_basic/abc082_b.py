s=sorted(input())
t=sorted(input())

if s<t[::-1]:
    print('Yes')
else:
    print('No')