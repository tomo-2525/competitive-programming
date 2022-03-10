n, q = map(int, input().split())

s = [[] for _ in range(n)]

for i in range(q):
    query = list(map(int, input().split()))

    if query[0] == 0:
        s[query[1]].append(query[2])
    elif query[0] == 1:
        if len(s[query[1]]) != 0:
            tmp = s[query[1]].pop()
            s[query[1]].append(tmp)
            print(f"{tmp}")

    else:
        if len(s[query[1]]) != 0:
            s[query[1]].pop()


