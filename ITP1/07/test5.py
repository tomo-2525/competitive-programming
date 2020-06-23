lst1 = [0, 1, 2, 3]

lst2 = lst1.copy()  # lst1をコピー
lst3 = lst1

# lst1, lst2は同じ内容[0, 1, 2, 3]リストだが別のリストを保持している。
print('lst1:', lst1)  # 出力：lst1: [0, 1, 2, 3]
print('lst2:', lst2)  # 出力：lst2: [0, 1, 2, 3]
print('lst3:', lst3)  # 出力：lst3: [0, 1, 2, 3]

# lst2とlst3の最初の要素を-1にする
lst2[0] = -1
lst3[0] = -1
print('lst1:', lst1)  # 出力：lst1: [0, 1, 2, 3]
print('lst2:', lst2)  # 出力：lst2: [-1, 1, 2, 3]
print('lst3:', lst3)  # 出力：lst3: [-1, 1, 2, 3]
