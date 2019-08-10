h,w=map(int,input().split())

s=['0'*(w+2)]

for i in range(h):
    s.append('0'+input()+'0')

s.append('0'*(w+2))


ans=[]
for i in range(1,h+1):
    tmp=[]
    for j in range(1,w+1):
        if s[i][j]=='#':
            tmp.append('#')
        else:
            tmp.append([s[i-1][j-1],s[i-1][j],s[i-1][j+1],\
            s[i][j-1],s[i][j],s[i][j+1],\
            s[i+1][j-1],s[i+1][j],s[i+1][j+1]].count('#'))
    ans.append(tmp)
for i in range(h):
    print(''.join(map(str,ans[i])))