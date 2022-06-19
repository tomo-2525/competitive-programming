n, m = map(int, input().split())
G = [[] for i in range(n)]
for i in range(m):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  G[a].append(b)
  G[b].append(a)


# print(G)
que =[0] 
dist = [-1]*n
dist[0] = 0
cnt = [0]*n # 最短経路の個数
cnt[0] = 1
 
# BFS
for cur in que:
  for nxt in G[cur]:
    if dist[nxt] == -1: # 訪れてなかったら
      que.append(nxt)
      dist[nxt] = dist[cur]+1
      cnt[nxt] = cnt[cur]
    elif dist[nxt] == dist[cur]+1:
      cnt[nxt] += cnt[cur]
      cnt[nxt] %= 10**9+7

print(cnt)
print(cnt[-1])
