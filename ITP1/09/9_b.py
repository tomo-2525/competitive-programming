while True:
    s = input()
    if s == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        tmp = s[:h]
        s = s[h:] + tmp
    print(f"{s}")

"""
別解
while 1:
    C = input()
    if C == "-":
        break
    N = int(input())
    for i in range(N):
        H = int(input())
        C = C[H:] + C[:H]
    print(C)
"""
