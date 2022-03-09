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
