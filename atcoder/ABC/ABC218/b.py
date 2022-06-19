P = list(map(int, input().split()))
A = [x for x in "abcdefghijklmnopqrstuvwxyz"]

for i in P:
    print(f"{A[i-1]}",end="")
print()