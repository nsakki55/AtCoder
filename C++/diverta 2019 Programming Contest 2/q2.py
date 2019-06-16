import sys
import numpy as np

def main():
    n=int(input())
    ball=[]
    for i in range(n):
        temp_list=list(map(int,input().split()))

        ball.append(temp_list)
    
    diff_list=[]
    for j in range(n-1):
        
        temp_diff=np.array(ball[j+1])-np.array(ball[j])
        
        diff_list.append(list(temp_diff))

    count=[]
    for i in range(len(diff_list)):
        count.append(diff_list.count(diff_list[i]))

    max_index=np.argmax(count)
    
    max_pair=diff_list[max_index]
    

    loss=1
    for i in range(len(diff_list)):
        if(diff_list[i])!=max_pair:
            loss+=1
    print(loss)

if __name__=="__main__":
    main()