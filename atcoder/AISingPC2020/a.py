l, r, d = map(int, input().split())

flag = 0

for i in range(l, r + 1):
    if i % d == 0:
        flag += 1

print(flag)

"""
l, r, d = map(int, input().split()) 
print(r//d - (l-1)//d)
"""
