from operator import length_hint
from sys import stdin
# f_i = stdin
# q = f_i.readline()
q = int(input())

d = 0

from collections import deque
L = deque()

for _ in range(q):
    l = input()
    if  l[0] == "0":
        L.append(l[2:])
    elif l[0] == "1":
        r = int(l[2:])
        L.rotate(r)
        d -= r
    else:
        L.pop()
L.rotate(d)
L.reverse()

for i in range(len(L)):
    print(L[i])




"""
未実装
class List:
    data = []
    index = -1

    def insert(self, x):
        self.data.insert(self.index, x)
        self.index = self.data.index(x)
        print(f"{self.data} {self.index}")

    def move(self, d):
        self.index += d

        print(f"{self.data} {self.index}")

    def erase(self):
        del self.data[self.index]

        if self.index < len(self.data)-1:
            self.index += 1
        else:  # comparing index
            self.index = len(self.data)-1
        print(f"{self.data} {self.index}")


q = int(input())
l = List()

for i in range(q):
    order = input().split()

    if order[0] == "0":
        x = int(order[1])
        print(f"insert {x}")
        l.insert(x)
        print()

    elif order[0] == "1":
        x = int(order[1])
        print(f"move {x}")
        l.move(x)
        print()

    elif order[0] == "2":
        print(f"erase")
        l.erase()
        print()

for i in range(len(l.data)):
    print(l.data[i])

"""
