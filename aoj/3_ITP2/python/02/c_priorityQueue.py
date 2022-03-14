import heapq

n, q = map(int, input().split())

pq = [[] for _ in range(n)]


for i in range(q):
    query = input()
    if query[0] == "0":
        _, t, x = map(int, query.split())
        heapq.heappush(pq[t], -x)

    elif query[0] == "1":
        _, t= map(int, query.split())
        if len(pq[t]) != 0: 
            # tmp = heapq.heappop(pq[t])
            # heapq.heappush(pq[t], -1*tmp)
            # print(-tmp)
            print(-pq[t][0])

    elif query[0] == "2":
        _, t= map(int, query.split())
        if len(pq[t]) != 0: 
            heapq.heappop(pq[t])



