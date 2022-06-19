import sys

N, M = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort()

x, y = 0,0
ans = sys.maxsize
while (x < N) and (y < M) :
		ans = min(ans, abs(A[x] - B[y]))
		if (A[x] > B[y]): y+=1
		else: x+=1
print(ans)