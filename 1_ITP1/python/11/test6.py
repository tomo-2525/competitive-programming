def hoge(a, b, **vars):
    print(a, b, vars)


print(1, 2, c=2, d=3, e=4)
# hoge(1, 2, c=2, d=3, e=4)  # 出力：1 2 {'c': 2, 'd': 3, 'e': 4}
