W = input()
count = 0
while True:
    T = input().split()
    if T[0] == "END_OF_TEXT":
        break
    for i in T:
        if i == W or i.lower() == W:
            count += 1
print(count)

"""
別解
import sys
w=input()
print(sys.stdin.read().lower().split().count(w))
"""
