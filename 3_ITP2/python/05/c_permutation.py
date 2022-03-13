from itertools import permutations

N = int(input())
A = tuple(map(int, input().split()))

*PS, = permutations(range(1, N+1), r=N)
# tmp = list(permutations(range(1, N+1), r=N))

i = PS.index(A)
if i > 0:
    print(*PS[i-1])

print(*A)

if i < len(PS)-1:
    print(*PS[i+1])

# i = tmp.index(A)
# if i > 0:
#     print(*tmp[i-1])
# print(*A)
# if i < len(tmp)-1:
#     print(*tmp[i+1])


"""
p = [1, 2]
*x, = p 
print(x == p)
print(x is p)

x = p
print(x == p)
print(x is p)
"""

"""
== 同じ値かどうか
is 同じオブジェクトであるかどうか(id関数の戻り値で比較)
"""