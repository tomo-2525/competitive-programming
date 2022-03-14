# -*- coding: utf-8 -*-
import sys
# input = sys.stdin.readline

Q = int(input())
A = []
ans = []

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 0:
        A.append(q[1])
    elif q[0] == 1:
        # ans.append(A[q[1]])
        print(A[q[1]])
    else:
        A.pop()

# print(*ans,sep='\n')


""""
class vector:
    data = []

    def pushBack(self, x):
        self.data.append(x)

    def randomAccess(self, p):
        return self.data[p]

    def popBack(self):
        deta_index = len(self.data)-1
        del self.data[deta_index]


q = int(input())
v = vector()

for i in range(q):
    order = input().split()

    if order[0] == "0":
        x = int(order[1])
        v.pushBack(x)

    elif order[0] == "1":
        x = int(order[1])
        data = v.randomAccess(x)
        print(data)

    elif order[0] == "2":
        v.popBack()
"""