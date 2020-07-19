
from collections import deque
Q = deque()
q = int(input())
for i in range(q):
    a = input()
    if a[0] == '0':  # pushBack
        if a[2] == '0':
            Q.appendleft(a[4:])
        else:
            Q.append(a[4:])
    elif a[0] == '1':
        print(Q[int(a[2:])])  # randomAccess
    else:  # popBack
        if a[2] == '0':
            Q.popleft()
        else:
            Q.pop()

"""class deque:
    data = []

    def push(self, d, x):
        if d == 0:
            self.data.insert(0, x)
        if d == 1:
            deta_index = len(self.data)
            self.data.append(x)

    def randomAccess(self, p):
        print(self.data[p])

    def pop(self, d):
        if d == 0:
            del self.data[0]
        if d == 1:
            deta_index = len(self.data) - 1
            del self.data[deta_index]


q = int(input())
deque = deque()

for i in range(q):
    order = input().split()

    if order[0] == "0":
        d = int(order[1])
        x = int(order[2])
        deque.push(d, x)

    elif order[0] == "1":
        p = int(order[1])
        deque.randomAccess(p)

    elif order[0] == "2":
        d = int(order[1])
        deque.pop(d)
"""
