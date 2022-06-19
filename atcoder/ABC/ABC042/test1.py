N = 2000
N = str(N)
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(len(a)):
    print(a[i])
    print(N)
# if str(a[i]) in N:
#     print(a[i])
#     print(N)


N, K = map(int, input().split())
out = N
N = str(N)
a = list(map(int, input().split()))
while 1 < 2:
    N1 = N
    i = 0
    for i in range(len(a)):
        if str(a[i]) in N:
            N = int(N)
            N += 1
            N = str(N)
    if N1 == N:
        break

print(N)
# print(N)
