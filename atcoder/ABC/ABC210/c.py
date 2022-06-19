N, K = map(int, input().split())
C = [x for x in str(input())]
ans = 0
for i in range(N-K+1):
    ans = max(ans, len(set(C[i:i+K+1])))

print(ans)
