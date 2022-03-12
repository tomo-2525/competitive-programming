n = int(input())
A = list(map(int, input().split()))
q = int(input())

for i in range(q):
    op = list(map(int, input().split()))
    if op[0] == 0:
        print(min(A[op[1]:op[2]]))
    else:
        print(max(A[op[1]:op[2]]))
