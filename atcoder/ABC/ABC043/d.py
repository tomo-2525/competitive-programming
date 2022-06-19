S = input()

s = "abcdefgfijklmnopqrstuvwxyz"
count = [0 for _ in range(26)]
for i in S:
    count[s.find(i)] += 1
    moji = count.index(max(count))

flag = 0
for i in range(len(S)):
    if flag == 1:
        break
    for j in range(len(S)):
        tmp = S.count(s[moji], i, j)
        if tmp > (len(S[i:j]) // 2):
            print(i, j)
            flag = 1
            break
if flag == 0:
    print("-1 -1")
    解けなかった

"""
以下、文字列 s の長さを n とします。s には、長さ 2 以上の部分文字列が n(n-1)/2 個存在します。
部分点のデータセットでは n が最大で 100 と小さいため、s の部分文字列をすべて 列挙することができます。
それぞれの部分文字列について、各アルファベットの出 現回数を数えることでアンバランスか判定すれば、時間計算量 O(n^3) で問題を解く ことができます。
満点を得るためには、n が 10^5 に達するケースにも正解する必要があります。この n の値では、すべての部分文字列を列挙する時間はありません。
どうすればよいでしょうか?
実は、長さ 2 の "XX"(X は何らかの同じアルファベット)というパターンと、
長さ 3 の "XYX"(Y は何らかのアルファベット)というパターンのいずれも s に存在しなければ、
アンバランスな部分文字列は存在しません。
なぜなら、もしこれらのパターンが存在しなければ、
同じアルファベットの 2 つの文字の間に必ず他の文字が 2つ以上挟 まっていることになり、
一種類のアルファベットが部分文字列の文字の過半数を占め ることはないからです。よって、時間計算量 O(n) で問題を解くことができます。
"""

"""
import sys
s = input()
l = len(s)
if l == 2:
    if s[0] == s[1]:
        print(1, 2)
        sys.exit()
    else:
        print('-1 -1')
        sys.exit()
for i in range(l - 2):
    s1 = s[i]
    s2 = s[i + 1]
    s3 = s[i + 2]
    if s1 == s2 or s1 == s3 or s2 == s3:
        print(i + 1, i + 3)
        sys.exit()
print('-1 -1')

"""
