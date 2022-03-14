import sys

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
table = [0 for i in range(26)]
#input_str = input()
input_str = sys.stdin.read()

for i in input_str:
    index = 0
    for j in letters:
        #print(i, j)
        if i == j:
            table[index % 26] += 1
        index += 1

for i in range(26):
    print(f"{letters[i]} : {table[i]}")


"""
別解１
import sys
table = [0]*26

letters = "abcdefghijklmnopqrstuvwxyz"
input_str = sys.stdin.read()

for A in input_str:
    index = 0
    for B in letters:
        if A == B or A == B.upper():
            table[index] += 1
            break
        index += 1

for i in range(len(letters)):
    print("%s : %d" % (letters[i], table[i]))

別解２
from string import ascii_lowercase, ascii_uppercase
s = open(0).read()
ans = [0]*26
for c in s:
    i = ascii_lowercase.find(c)
    if i > -1:
        ans[i] += 1
    i = ascii_uppercase.find(c)
    if i > -1:
        ans[i] += 1
for c, t in zip(ascii_lowercase, ans):
    print("%s : %d" % (c, t))

別解３
import sys
 
cnt = {}
 
for line in sys.stdin:
  for l in line:
    if l.isalpha():
      c = l.lower()
      cnt[c] = cnt.get(c,0)+1
 
for i in range(26):
  c = chr(ord('a')+i)
  print( c, " : ", cnt.get(c,0), sep = '' )

ファイルの読み込みと標準入力
http://osksn2.hep.sci.osaka-u.ac.jp/~taku/osx/python/readfile.html
"""
