def main():

    n,x=list(map(int,input().split()))
    point=list(map(int,input().split()))

    jump=[0]
    sum=0
    for i in range(n):
        sum+=point[i]
        jump.append(sum)

    count=0
    for k in range(n+1):
        if jump[k]<=x:
            count+=1
    print(count)
    print(jump)
    
if __name__=="__main__":
    main()