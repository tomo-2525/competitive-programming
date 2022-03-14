# q = int(input())
# S = set()

# for i in range(q):
#     op, x = map(int, input().split())
#     if op == 0:
#         S.add(x)
#         print(len(S))
#     elif op == 1:
#         print(int(x in S)) # countの仕方
#     elif op == 2:
#         if x in S:
#             S.remove(x)
#     else:
#         L, R = op, x
#         if R - L < len(S):
#             for i in [i for i in range(L, R+1) if i in S]: print(i)
#         else:
#             for i in sorted([i for i in S if L <= i <= R]): print(i)
#         continue
#         x = int(l[2:])


import sys

s = set()
input()

for q in sys.stdin:
    q = q.split()
    if q[0] == '0':
        s.add(int(q[1]))
        print(len(s))
    elif q[0] == '1':
        print(int(int(q[1]) in s))
    elif q[0] == '2':
        s.discard(int(q[1]))
    else:
        ans = []
        if len(s) > int(q[2]) - int(q[1]): # L - R
            for i in range(int(q[1]), int(q[2])+1):
                if i in s:
                    print(i)
        else:
            for i in s:
                if int(q[1]) <= i <= int(q[2]):
                    ans.append(i)
    
            for i in sorted(ans):
                print(i)
