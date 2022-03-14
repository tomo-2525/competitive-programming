r, c = map(int, input().split())

m = [list(map(int, input().split())) for i in range(r)]

for i in range(r):
    sum = 0
    for j in range(c):
        sum += m[i][j]
    m[i].append(sum)

l = []
for i in range(c+1):
    sum = 0
    for j in range(r):
        sum += m[j][i]
    l.append(sum)

m = m+[l]

# print(l)
# print(m)

for i in range(r+1):
    for j in range(c + 1):
        if j == c:
            print(f"{m[i][j]}", end="")
        else:
            print(f"{m[i][j]} ", end="")
    print()

"""
配列への要素の追加
http://taustation.com/python3-2d-array-adding-row-column/#i-4
"""
