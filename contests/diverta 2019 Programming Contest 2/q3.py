def main():
    n=int(input())
    num=list(map(int,input().split()))

    for i in range(n-1,0,-1):
        print(i)

if __name__=="__main__":
    main()