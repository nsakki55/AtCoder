
def main():
    n,m=list(map(int,input().split()))

    S=list(map(int,input().split()))    

    T=list(map(int,input().split()))
    part_T=[[]]
    part_S=[[]]

    print([1,2]==[1,2])
    for i in range(n):
        for j in range(0,n-i):

            part_S.append(S[i:j+i+1])


    for i in range(m):
        for j in range(0,n-i):

            part_T.append(T[i:j+i+1])
    
    count=0
    for i in range(len(part_S)):
        for j in range(len(part_T)):
     #       print(part_S[i])
     #       print(part_T[j])
            if(part_S[i]==part_T[j]):
                count+=1
    
    #print(part_S)
    #print(part_T)
    print(count)  
    
if __name__=="__main__":
    main()