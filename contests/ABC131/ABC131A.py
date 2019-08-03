
num=str(input())

lst=[]

while num>0:
    lst.append(num%10)
    num//=10
lst.reverse()

l=0
flag=True
for index,i_num in enumerate(lst):
    print(index,i_num)
    if flag:
        if index==0:
            l=i_num
        else:
            if i_num==l:
                print("Bad")
                flag=False
                break
            l=i_num

if flag:
    print("Good")            
