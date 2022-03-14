n = int(input())
l = []

for i in range(n):
    v, w, t, d, s = input().split()
    l.append((int(v), int(w), t, int(d), s))

l.sort()
for i in l:
    print(*i)

