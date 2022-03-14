while True:

    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    for i in range(a):
        for j in range(b):
            if (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
                print(".", end="")
            else:
                print("#", end="")

        print()
    print()

"""
別解１
while True:
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        for k in range(W):
            if (i+k)%2 == 0:
                print("#",end = "")
            else:
                print(".",end = "")
        print()

    print() #データセットの区切り
"""
