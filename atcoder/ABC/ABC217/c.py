N = int(input())
P = list(map(int, input().split()))
Q = [0] * N

for i in range(N):
    Q[P[i]-1] = i+1

for i in range(N):
    if i == N-1:
        print(f'{Q[i]}',end='')
    else:    
        print(f'{Q[i]} ',end='')

print()