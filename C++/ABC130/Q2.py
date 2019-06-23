def main():

    w,h,x,y=list(map(int,input().split()))


    if(x==w/2 and y==h/2):
        s=w*h/2
        print(s,1)
    
    elif(x==w/2 or y==h/2):
        s=w*h/2
        print(s,0)

    elif(y==(h/w)*x or y==-(h/w)*x):
        s=w*h/2
        print(s,0)
   
    else:
        s_11=w*(h-y)
        s_12=w*y
        S1=min([s_11,s_12])

        s_21=h*x
        s_22=h*(w-x)
        S2=min([s_21,s_22])

        #if S1==S2:
        #    S=w*h/2
        #    print(S,0)
        #else:
        S=max([S1,S2])
        print(S,0)

if __name__=="__main__":
    main()