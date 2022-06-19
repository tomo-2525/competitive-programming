N, A, X, Y = map(int, input().split())

sum = 0
if N <= A:
    sum += N * X
elif N > A:
    sum += A * X
    sum += (N-A) * Y 
print(sum)