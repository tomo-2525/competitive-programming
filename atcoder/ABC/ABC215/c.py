import itertools

s, k  = input().split()
l = list(i for i in s)
k = int(k)

dic = list(set(list(itertools.permutations(l))))
l = []
for i in dic:
    s = "".join(str(x) for x in i)
    l.append(s)
l.sort()
print(l[k-1])


# 自分の実装
# import itertools
# s, k  = input().split()
# l = list(i for i in s)
# k = int(k)

# dic = list(itertools.permutations(l))

# l = []
# for i in dic:
#     s = "".join(str(x) for x in i)
#     if s not in l:
#         l.append("".join(str(x) for x in i))
# l.sort()
# print(l[k-1])


# 解答
# import itertools
# S, K = input().split()
# K = int(K)
# list_S = sorted(["".join(s) for s in list(set(list(itertools.permutations(list(S)))))])
# print(list_S[K - 1])