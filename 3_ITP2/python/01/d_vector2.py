n, q = map(int, input().split())

v = [[] for _ in range(n)]

for i in range(q):
    query = input()
    if query[0] == "0":
        _, n, x = map(int, query.split())
        v[n].append(x)
    elif query[0] == "1":
        _, n = map(int, query.split())
        if len(v[n]) == 0:
            print()
        else:
            for j,k in enumerate(v[n]):
                if j == 0:
                    print(f"{k}",end="")
                else:
                    print(f" {k}",end="")
            print()
    else:
        _, n = map(int, query.split())
        v[n].clear()