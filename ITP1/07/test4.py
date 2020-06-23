l = [1, 8, 27, 65, 125]  # 3番目の要素を置き換えたい
l[3] = 4 ** 3  # 　3番目の要素を4の3乗に置き換える
print(l)

a = ["AB", "CD", "EF", "GH"]
print(a)

# リストaの２番目の要素を削除する。削除すると要素数が減る
del a[1]
print(a)

a.clear()
print(a)

a = ["AB", "CD", "EF", "GH"]
a = []
print(a)
