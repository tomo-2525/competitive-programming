# 自分の
import bisect
L, Q = map(int, input().split())

t = [0, L]
for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        t.append(x)
        t.sort()
    else:
        index = bisect.bisect(t,x)
        print(t[index] -  t[index-1]   )

# 自分の改善
import bisect
L, Q = map(int, input().split())

t = [0, L]
for i in range(Q):
    c, x = map(int, input().split())
    index = bisect.bisect(t,x)
    if c == 1:
        t.insert(index,x)
    else:
        print(t[index] -  t[index-1]   )


# 解答
from bisect import *
import array 
L,Q=map(int,input().split())
D=array.array('i',[0,L])
for i in range(Q):
  c,x=map(int,input().split())
  j=bisect(D,x)
  if c==1:D.insert(j,x)
  else:print(D[j]-D[j-1])