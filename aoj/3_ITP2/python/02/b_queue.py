from collections import deque
import queue

n, q = map(int, input().split())
queue = [deque() for _ in range(n)]

for i in range(q):
    query = input()
    if query[0] == "0":
        _, t, x = map(int, query.split())
        queue[t].append(x)

    elif query[0] == "1":
        _, t = map(int, query.split())
        if len(queue[t]) != 0:
            print(queue[t][0])
    
    elif query[0] == "2":
        _, t = map(int, query.split())
        if len(queue[t]) != 0:
            queue[t].popleft()