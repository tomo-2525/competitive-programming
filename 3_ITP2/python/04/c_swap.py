n = int(input())
A = list(map(int, input().split()))
q = int(input())


for i in range(q):
    b, e, t = map(int , input().split())
    for k in range(e-b):
        tmp = A[b+k]
        A[b+k] = A[t+k]
        A[t+k] = tmp
    
print(*A)