s=input()
k=int(input())

if k<=len(s):
    total=[s[i:i+k] for i in range(0,len(s),1) if i+k<=len(s)]
    print(len(set(total)))

else:
    print(0)