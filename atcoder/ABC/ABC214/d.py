import sys
input = sys.stdin.readline
N = int(input())
 
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.root = [-1] * (n + 1)
    self.rnk = [0] * (n + 1)
  def Find_Root(self, x):
    if self.root[x] < 0:
      return x
    else:
      self.root[x] = self.Find_Root(self.root[x])
      return self.root[x]
  def Unite(self, x, y):
    x = self.Find_Root(x)
    y = self.Find_Root(y)
    if x == y:
      return 
    elif self.rnk[x] > self.rnk[y]:
      self.root[x] += self.root[y]
      self.root[y] = x
    else:
      self.root[y] += self.root[x]
      self.root[x] = y
      if self.rnk[x] == self.rnk[y]:
        self.rnk[y] += 1
  def SameQuery(self, x, y): return self.Find_Root(x) == self.Find_Root(y)
  def Count(self, x): return -self.root[self.Find_Root(x)]
 
uf = UnionFind(N)
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

edges.sort(key = lambda x: x[2])
res = 0
for x, y, w in edges:
  if uf.SameQuery(x, y) == False:
    res += uf.Count(x) * uf.Count(y) * w
    uf.Unite(x, y)
print(res)