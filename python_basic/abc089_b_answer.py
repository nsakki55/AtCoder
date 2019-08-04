input()
l=map(str,input().split())

print('Three' if len(set(l))==3 else 'Four')