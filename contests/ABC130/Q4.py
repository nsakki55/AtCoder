
def main():
    n,k=list(map(int,input().split()))

    array=list(map(int,input().split()))

    count=0
    for i in range(n):
        for j in range(0,n-i):

            wa=sum(array[i:j+i+1])
 
            if(wa>=k):
                count+=1

    print(count)  
    
if __name__=="__main__":
    main()