
def main():

    n=int(input())
    p=list(map(int,input().split()))

    cnt=0
    for i in range(n-2):
        
        tmp=[p[i],p[i+1],p[i+2]]
        tmp.sort()
        if p[i+1]==tmp[1]:
            cnt+=1
    print(cnt)




if __name__=='__main__':
    main()