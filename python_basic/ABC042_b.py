n,l=map(int,input().split())

string=[]
for s in range(n):
    string.append(str(input()))
string.sort()
print(''.join(string))