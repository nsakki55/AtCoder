import datetime

s=list(map(int,input().split('/')))

s=datetime.date(s[0],s[1],s[2])
print('Heisei' if s<=datetime.date(2019,4,30) else 'TBD')