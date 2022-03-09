n, m, l = map(int, input().split())
"""
a = [[map(int, input().split())]for i in range(m)]
b = [[map(int, input().split())] for i in range(l)]
#[[<map object at 0x7f9deda211c0>], [<map object at 0x7f9deda210d0>]]
#[[<map object at 0x7f9deda21250>], [<map object at 0x7f9deda21310>], [<map object at 0x7f9deda21370>]]
"""

a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split()))for i in range(m)]
# print(a) [[1, 2], [0, 3], [4, 5]]
# print(b) [[1, 2, 1], [0, 3, 2]]

for i in range(n):
    for j in range(l):
        sum = 0
        for k in range(m):
            sum += a[i][k] * b[k][j]
        if j == l - 1:
            print(f"{sum}", end="")
        else:
            print(f"{sum} ", end="")
    print()
