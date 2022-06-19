# 自分の実装
Q = int(input())
L = []
R = []
for _ in range(Q):
    query = input()
    if query[0] == '1':
        _, n = map(int,query.split())
        L.append(n)
    elif query[0] == '2':
        _, n = map(int,query.split())
        for i in range(len(L)):
            L[i] += n
    else:
        R.append(min(L))
        L.remove(min(L))

for i in R:
    print(i)

# 
from heapq import*
h=[];d=0
for _ in range(int(input())):
	q=input().split()
	if q[0]=='1':heappush(h,int(q[1])-d)
	elif q[0]=='2':d+=int(q[1])
	else:print(heappop(h)+d)