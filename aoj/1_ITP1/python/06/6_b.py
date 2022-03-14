n = int(input())

l = [0 for i in range(52)]
# print(l)

for i in range(n):
    char, num = input().split()
    num = int(num)

    if char == "S":
        l[num - 1] = 1

    elif char == "H":
        l[num-1+13] = 1

    elif char == "C":
        l[num-1+26] = 1

    elif char == "D":
        l[num-1+39] = 1

for i in range(52):
    if l[i] == 0:
        if 0 <= i and i <= 12:
            print(f"S {i+1}")
        if 13 <= i and i <= 25:
            print(f"H {i+1-13}")
        if 26 <= i and i <= 38:
            print(f"C {i+1-26}")
        if 39 <= i and i <= 51:
            print(f"D {i+1-39}")

"""
別解1
cards = list()
suit = ['S', 'H', 'C', 'D']
n = int(input())
for i in range(n):
    s,r = input().split()
    r = int(r)
    if s == "S": cards.append(0 + r)
    elif s == "H": cards.append(13 + r)
    elif s == "C": cards.append(26 + r)
    elif s == "D": cards.append(39 + r)
for i in range(1,53):
    if not (i in cards):
        print(suit[(i-1)//13], (i-1)%13+1)

別解２
import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001


suits = ["S","H","C","D"]
check = [[False]*14 for _ in range(4)]


def get_row(arg_ch):
    for i in range(len(suits)):
        if arg_ch == suits[i]:
            return i


N = int(input())

for _ in range(N):
    tmp = input().split()
    check[get_row(tmp[0])][int(tmp[1])] = True


for row in range(4):
    for col in range(1,14):
        if check[row][col] == False:
            print("%s %d"%(suits[row],col))

"""
