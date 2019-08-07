n=input()
print( 'Yes' if int(n)%sum(map(int,list(n)))==0 else 'No')