N = int(input())
a = list(map(int, input().split()))

flag = 0
for i in range(0, N, 2):
    if a[i] % 2 == 1:
        flag += 1

print(flag)
