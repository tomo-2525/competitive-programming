n = int(input())
tp = 0
hp = 0

for i in range(n):
    l = input().split()
    if l[0] == l[1]:
        tp += 1
        hp += 1

    elif l[0] > l[1]:
        tp += 3

    elif l[0] < l[1]:
        hp += 3

print(f"{tp} {hp}")
"""


文字列比較
https://note.nkmk.me/python-str-compare/
"""
