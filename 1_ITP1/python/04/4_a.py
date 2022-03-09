# 入力）3 2
a, b = map(int, input().split())

# print(f"{a//b} {a%b} {a/b}")  # 1 1 1.5
print(f"{a//b} {a%b} {a/b:.6f}")  # 1 1 1.500000 小数点以下の桁数６
