N=int(input())
A=list(map(int,input().split()))
print(' '.join(map(str,A[::-2]+A[N%2::2])))