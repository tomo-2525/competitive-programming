# 自分の解答
H, W, N = map(int, input().split())

H = [1] * H
W = [1] * W
L = []
for _ in range(N):
    A, B = map(int, input().split())
    L.append([A,B])
    H[A-1] = 0
    W[B-1] = 0 

for i in range(N):
    print(L[i][0]-sum(H[:L[i][0]]), L[i][1]-sum(W[:L[i][1]]))




# 解説　座標圧縮
H,W,N=map(int,input().split())
X,Y=[],[]
for i in range(N):
  x,y=map(int,input().split())
  X.append(x)
  Y.append(y)
Xdict = {x:i+1 for i,x in enumerate(sorted(list(set(X))))}
Ydict = {y:i+1 for i,y in enumerate(sorted(list(set(Y))))}
for i in range(N):
  print(Xdict[X[i]], Ydict[Y[i]])