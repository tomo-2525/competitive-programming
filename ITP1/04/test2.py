# 例）入力：1.4 2.3 4.3
l1 = map(float, input().split())
print(l1)  # 出力：<map object at 0x7fb576accc50>
l2 = [float(x) for x in l1]
print(l2)  # 出力：[1.4, 2.3, 4.3]
l3 = list(map(float, l1))
print(l3)  # 出力：[]

l1 = list(map(float, input().split()))
print(l1)  # 出力：[1.4, 2.3, 4.3]
l2 = [float(x) for x in l1]
print(l2)  # 出力：[1.4, 2.3, 4.3]
l3 = list(map(float, l1))
print(l3)  # 出力：[1.4, 2.3, 4.3]
