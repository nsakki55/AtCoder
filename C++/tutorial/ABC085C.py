n,y=map(int,input().split())

max_x=y//10000
max_y=y//5000
max_z=y//1000

list=[]

# 多重ループを無駄に繰り返すと処理が糞重くなる

flag=False
for x_i in reversed(range(0,n+1)):
    for y_i in reversed(range(0,n+1)):
        z_i=n-x_i-y_i
        if z_i>=0 and y_i>=0:
            total=10000*x_i+5000*y_i+1000*z_i
            if total==y:
                list.append(x_i)
                list.append(y_i)
                list.append(z_i)

# 多重ループからの抜け出し方
                flag=True
                break
        if flag:
            break




if len(list)==0:
    for i in range(0,3):
      list.append(-1)

print("{} {} {}".format(list[0],list[1],list[2]))

