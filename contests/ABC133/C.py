def main():
    L,R=map(int,input().split())
    
    min_n=L*(L+1)
    
    
    flag=True
    mod=2019
    if flag:
        for i in range(L,R+1):
            if i%2019 ==0:
                flag=False
                mod=0
            else:
                for j in range(L+1,R+1):
                    tmp=i*j
                    mod=min(mod,tmp)
                    if mod==1:
                        flag=False        
    if flag:
        print(min_n%2019)
    else:
        print(mod)    

if __name__=="__main__":
    main()