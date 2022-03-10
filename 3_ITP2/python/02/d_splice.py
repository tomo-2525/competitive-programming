import sys
from collections import defaultdict, deque
sys.stdin.readline().split()
A = defaultdict(deque)
ans = []
for query in sys.stdin:
    if query[0] == '0':
        t, x = query[2:].split()
        A[t].append(x)
    elif query[0] == '1':
        ans.append(' '.join(A[query[2:-1]]) + '\n')
    else:
        s, t = query[2:].split()
        if A[t]:
            if len(A[s]) == 1:
                A[t].append(A[s][0])
            elif len(A[t]) == 1:
                A[s].appendleft(A[t][0])
                A[t] = A[s]
            else:
                A[t].extend(A[s])
        else:
            A[t] = A[s]
        A[s] = deque()
sys.stdout.writelines(ans)


"""n, q = map(int, input().split())

L = [[] for _ in range(n)]

for i in range(q):
    query = input()
    if query[0] == "0":
        _, t, x = map(int, query.split())
        L[t].append(x)
    
    elif query[0] == "1":
        _, t = map(int, query.split())
        print(*L[t])
        # for j, num in enumerate(L[t]):
        #     if j==0:
        #         print(f'{num}', end='')
        #     else:
        #         print(f' {num}', end='')
        # print()

    elif query[0] == "2":
        _, s, t = map(int, query.split())
        L[t].extend(L[s])
        L[s] = []
"""
