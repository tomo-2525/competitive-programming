import math
while True:
    n = int(input())
    if n == 0:
        break
    a = 0
    l = list(map(int, input().split()))
    m = sum(l)
    m = m / n
    for i in l:
        a += math.pow(i-m, 2)
    a /= n
    a = math.sqrt(a)
    print(a)
