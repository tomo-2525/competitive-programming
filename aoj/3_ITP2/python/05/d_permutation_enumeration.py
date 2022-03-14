from itertools import permutations 

n = int(input())
ans = permutations(range(1,n+1), r=n)

for i in ans:
    print(*i)
