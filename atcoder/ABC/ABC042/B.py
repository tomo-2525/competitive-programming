N, L = map(int, input().split())
l = []
for i in range(N):
    s = input()
    l.append(s)
l.sort()
for i in l:
    print(f"{i}", end="")
print()

"""
sort()というメソッドがながら、使わなかったため無事死亡
N, L = map(int, input().split())
s_b = "zzzzzz"
l1 = []
l2 = []
for i in range(N):
    s = input()
    l1.append(s)

for i in range(N):
    for i in l1:
        if s_b > i:  
            s_b = i
    l2.append(l2)
"""
