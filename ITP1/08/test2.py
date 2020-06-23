a = ["AB", "CD", "EF", "GH"]
b = a[1:3]
print(b)
#['CD', 'EF']

c = a[:3]
print(b)
#['CD', 'EF']

d = a[1:]
print(b)
#['CD', 'EF']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
#['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 2番目から4番目を書き換える
letters[2:5] = ['C', 'D', 'E']
print(letters)
#['a', 'b', 'C', 'D', 'E', 'f', 'g']
# 2番目から4番目を削除する
letters[2:5] = []
print(letters)
#['a', 'b', 'f', 'g']
# リストの要素を全て削除する（空リストを作る）
letters[:] = []
print(letters)
[]
