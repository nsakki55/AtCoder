s=list(input())
l=[chr(i) for i in range(ord('a'),ord('z')+1) if chr(i) not in s]
print(sorted(l)[0] if len(l)>0 else 'None')