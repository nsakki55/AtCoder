import numpy as np 

def main():
    n,d=map(int,input().split())
    
    x=[]
    for i in range(n):
        tmp=list(map(int,input().split()))
        x.append(np.array(tmp))
    
   # print(x)

    cnt=0
    
    for k in range(n-1):
        for l in range(k+1,n):
            dist=np.sqrt(np.sum((x[k]-x[l])*(x[k]-x[l])))

            if float.is_integer(dist):
                cnt+=1

    print(cnt)

if __name__=="__main__":
    main()