
def main():
    S=list(map(str,input()))
    l_duplicate = [x for x in set(S) if S.count(x) ==2]
    print(l_duplicate)
    if len(l_duplicate)==2:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()