m, n = map(int, input().split())

#A = [[0 for i in range(n)] for i in range(m)]
# n次元配列A[i][j][k]の場合は、上のループはk, j, i
#
#A = [map(int, input().split()) for i in range(m)]
# print(A) #[<map object at 0x7fc6a1a59040>, <map object at 0x7fc6a1a59160>, <map object at 0x7fc6a1a592b0>]

A = [list(map(int, input().split())) for i in range(m)]
# print(A)

b = [int(input()) for i in range(n)]
# print(b)

for i in range(m):
    ans = 0
    for j in range(n):
        ans += A[i][j] * b[j]
    print(ans)
