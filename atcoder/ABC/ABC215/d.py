#解答
from math import *
 
N,M = map(int, input().split())
A = set(map(int, input().split()))

dp = [1]*(M+1)
dp[0]=0
for i in range(2,M+1):
	find = False
	for a in range(i,(10**5)+1,i):
		if a in A:
			find = True
			break
	if find:
		for a in range(i,M+1,i):
			dp[a] = 0
 
print(sum(dp))
for i in range(M+1):
	if dp[i]==1:
		print(i)


# 高宮くんのコード
# import math
# N, M = input().split()
# N = int(N)
# M = int(M)

# A = list(map(int, input().split()))
# S = list()

# for k in range(1, M+1):
#   frag = 1
#   for a in A:
#     if math.gcd(a, k) != 1:
#       frag = 0
#       break
#   if frag:
#     S.append(k)

# print(len(S))
# for s in S:
#   print(s)