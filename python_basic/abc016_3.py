n, m = map(int, input().split())
edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

friends = []
for i in range(1, n+1):
    friend = []
    for a, b in edges:
        if i == a:
            friend.append(b)
        elif i == b:
            friend.append(a)
    friends.append(friend)

for i in range(1, n+1):
    friend = friends[i-1]
    ff = []
    for f in friend:
        ff += friends[f-1]
    print(len(list(set(ff) - set([i]) - set(friend))))
