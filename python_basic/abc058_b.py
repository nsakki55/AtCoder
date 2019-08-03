pw=[input() for i in range(2)]
length=len(pw[0])
full_pw=[]
i=0
while i < length:
    full_pw.append(pw[0][i])
    if i <=len(pw[1])-1:
        full_pw.append(pw[1][i])
    i+=1

print(*full_pw,sep='')