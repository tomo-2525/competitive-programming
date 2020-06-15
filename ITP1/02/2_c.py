"""
だめだった
l = list(map(int, input().split()))
min = 10001
max = 0
mid = 0

for i in range(3):
    if max < l[i]:
        max = l[i]
    if min > l[i]:
        min = l[i]
print(f"{min} {max}")
for i in range(3):
    if l[i] <= max and l[i] >= min:
        mid = l[i]
print(f"{min} {mid} {max}")
"""

a, b, c = map(int, input().split())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)


"""
別解１
a,b,c = map(int, input().split())
if a > b: a,b = b,a
if b > c: b,c = c,b
if a > b: a,b = b,a
print(a, b, c)

別解２
ns=list(map(int,input().split()))
ns.sort()
print(ns[0],ns[1],ns[2])

別解３
print(*sorted(map(int,input().split())))
"""
