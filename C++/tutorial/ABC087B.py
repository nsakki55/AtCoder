a=int(input())
b=int(input())
c=int(input())
x=int(input())

b_count=x//100
c_count=x//50
a_count=x//500

num=0
try_count=0
for a_i in range(0,a+1,1):
    for b_i in range(0,b+1,1):
        for c_i in range(0,c+1,1):

            total=500*a_i+100*b_i+50*c_i
          #  print(total)
            #try_count+=1
            if total==x:
          #  print(a_i,b_i,c_i)
                num+=1

print(num)
#print("try count;{}".format(try_count))

