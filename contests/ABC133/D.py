import numpy as np

def main():

    n=int(input())

    a=list(map(int,input().split()))

    s=sum(a)

    x=[]

    #print(a[1:])

    x.append(s-2*sum(a[1:-1]))
    print(x[0])

    for i in range(n-1):
        x.append(2*a[i]-x[i])
    print(x)


if __name__=="__main__":
    main()