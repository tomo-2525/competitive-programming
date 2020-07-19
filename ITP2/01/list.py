readline = open(0).readline
writelines = open(1, 'w').writelines

Q = int(readline())
root = [None, None, None]
cursor = root[1] = [root, None, None]
# print(cursor)  #[[None, [...], None], None, None]


def insert(x):
    global cursor
    cursor[0][1] = cursor[0] = cursor = [cursor[0], cursor, x]
    print(cursor)


def move(d):
    global cursor
    if d > 0:
        for _ in range(d):
            cursor = cursor[1]
    else:
        for _ in range(-d):
            cursor = cursor[0]
    print(cursor)


def erase():
    global cursor
    cursor[1][0] = cursor[0]
    cursor[0][1] = cursor = cursor[1]
    print(cursor)


C = [insert, move, erase].__getitem__
for q in range(Q):
    t, *a = map(int, readline().split())
    C(t)(*a)
root = root[1]
print(root)
ans = []
while root[1]:
    ans.append("%d\n" % root[2])
    root = root[1]
writelines(ans)


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
