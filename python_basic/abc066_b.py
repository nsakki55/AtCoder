s=list(input())

for i in range(len(s)):

    if len(s)%2==0 and i!=0:
        if s[:int(len(s)/2)]==s[int(len(s)/2):]:
            print(len(s))
            break
    s.pop(-1)
