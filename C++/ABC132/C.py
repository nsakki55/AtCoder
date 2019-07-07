
def main():
    n=int(input())
    d=list(map(int,input().split()))

    d.sort()
    k=n//2
    
    num=d[k]-d[k-1]
    print(num)

if __name__=="__main__":
    main()
()
