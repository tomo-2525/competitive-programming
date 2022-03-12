n = int(input())
A = list(map(int, input().split()))
q = int(input())

for i in range(q):
    b, e = map(int, input().split())
    A[b:e] = reversed(A[b:e])
print(*A)