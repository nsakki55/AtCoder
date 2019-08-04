s=list(input())

a_indexes = [i for i, s in enumerate(s) if s == 'A']
z_indexes = [i for i, s in enumerate(s) if s == 'Z']
print(max(z_indexes)-min(a_indexes)+1)