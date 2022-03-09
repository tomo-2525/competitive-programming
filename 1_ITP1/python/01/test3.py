# 例）入力：1 2 3 4

l = input().split()
print(l)  # ['1', '2', '3', '4']

a, b, c, d = map(int, l)
print(f"{a} {b} {c} {d}")  # 1 2 3 4

l2 = list(map(int, l))
print(l2)  # [1, 2, 3, 4]

a, b, c, d = list(map(int, l))
print(f"{a} {b} {c} {d}")  # 1 2 3 4
