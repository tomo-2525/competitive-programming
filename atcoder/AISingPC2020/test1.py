def change_num(tmp, i):
    if tmp[i] == "0":
        return int(tmp, 2)+pow(2, N-i-1)
    else:
        return int(tmp, 2)-pow(2, N-i-1)


N = 4
tmp = "1010"
# print(tmp)
# tmp = bin(int(tmp[2:]))
# print(tmp[2:])
# tmp = tmp[2:]
# print(int(tmp, 2))
print(change_num(tmp, 0))
# print(popcount(7))
