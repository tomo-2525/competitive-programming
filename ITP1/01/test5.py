word = "Python"
print(f"Hello {word}")  # Hello Python
print(f"length: {len(word)}")  # length: 6
print(f"slice: {word[:2]}")  # slice: Py

pi = 3.14159265359
# そのまま表示
print(f"πの値は{pi}です")  # πの値は3.14159265359です

# 小数点以下2桁まで
print(f"πの値は{pi:.2f}です")  # πの値は3.14です

# 最大10桁で不足分は空白で埋める
print(f"πの値は{pi:10.2f}です")  # πの値は      3.14です

# 最大5桁で不足分は0で埋める
print(f"πの値は{pi:05.2f}です")  # πの値は03.14です

# 右寄せ 空白埋め
print(f"'{word:>10s}'")  # '    Python'

# 中央揃え
print(f"'{word:^10s}'")  # '  Python  '
