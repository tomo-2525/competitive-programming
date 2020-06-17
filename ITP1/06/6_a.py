n = int(input())
l = [int(x) for x in input().split()]
l.reverse()
# print(l)
j = 0

for i in l:
    if j != n-1:
        print(f"{i} ", end="")
    else:
        print(f"{i}", end="")
    j += 1
print()

"""
別解１
n = input()
a = list(map(int, input().split()))
a.reverse()
print(" ".join(map(str, a)))
#" ".join(map(str, a))は、リストaを空白区切りで、まとめている、
例えば、、
["1","2","3","4"]というリストがあれば、
"1 2 3 4"のようになる
"""
