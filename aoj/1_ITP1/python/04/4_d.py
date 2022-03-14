n = int(input())
l = list(map(int, input().split()))

min = min(l)
max = max(l)
sum = sum(l)

print(f"{min} {max} {sum}")

"""
別解１
BIG_NUM = 2000000000

N = int(input())

table = list(map(int,input().split()))

maximum = -BIG_NUM
minimum = BIG_NUM
total = 0

for x in table:
    if maximum < x:
        maximum = x
    if minimum > x:
        minimum = x
    total += x

print("%d %d %d"%(minimum,maximum,total))
"""
