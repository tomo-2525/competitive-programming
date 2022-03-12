from collections import deque
from sys import stdin
f_i = stdin

# n, q = map(int, f_i.readline().split())
n,q = map(int, input().split())
L = [deque() for i in range(n)]
ans = []

for op in (line.split() for line in f_i):
    op_type = op[0]
    if op_type == '0':
        L[int(op[1])].append(op[2])
    elif op_type == '1':
        ans.append(' '.join(L[int(op[1])]))
    else:
        s = int(op[1])
        ls = L[s]
        t = int(op[2])
        lt = L[t]
        if lt:
            if len(ls) == 1:
                lt.append(ls[0])
            elif len(lt) == 1:
                ls.appendleft(lt[0])
                L[t] = ls
            elif ls:
                lt.extend(ls)
        else:
            L[t] = ls
        L[s] = deque()
print('\n'.join(ans))


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
