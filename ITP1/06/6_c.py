l = [[[0 for i in range(10)] for i in range(3)] for i in range(4)]

n = int(input())

for i in range(n):
    b, f, r, v = map(int, input().split())
    l[b-1][f-1][r-1] += v


for i in range(4):
    for j in range(3):
        for k in range(10):
            print(f" {l[i][j][k]}", end="")
        print()
    if i != 3:
        print(20*"#")

"""
別解１
room = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
for i in range(4):
    for j in range(3):
        for k in range(10):
            room[i][j].append(0)
n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())
    room[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        print(" "+" ".join(map(str, room[i][j])))
    if i != 3: print("#"*20)
"""
