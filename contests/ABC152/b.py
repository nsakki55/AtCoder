a,b = input().split(' ')

str1 = a*int(b)
str2 = b*int(a)

print(sorted([str1, str2])[0])