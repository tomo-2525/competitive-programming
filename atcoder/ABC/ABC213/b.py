N = int(input())
L = list(map(int, input().split()))
L2 = sorted(L)
print(L.index(L2[N-2])+1)