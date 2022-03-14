s = input()
q = int(input())
insts = [input().split() for _ in range(q)]

for inst in insts:
    a, b = int(inst[1]), int(inst[2]) + 1
    if inst[0] == "replace":
        p = inst[3]
        s = s[:a] + p + s[b:]
    elif inst[0] == "reverse":
        s = s[:a] + s[a:b][::-1] + s[b:]
    elif inst[0] == "print":
        print(s[a:b])

"""
s = input()
q = int(input())
for i in range(q):
    l = input().split()
    l[1] = int(l[1])
    l[2] = int(l[2])

    if l[0] == "replace":
        tmp = s[l[1]: l[2] + 1]
        if l[1] == l[2]:
            tmp = s[l[1]]
        s = s.replace(tmp, l[3])
    elif l[0] == "reverse":
        tmp1 = s[l[1]:l[2]+1]
        tmp2 = tmp1[::-1]
        #print(f"tmp = {tmp}")
        s = s.replace(tmp1, tmp2)

    elif l[0] == "print":
        ans = s[l[1]:l[2]+1]
        print(f"{ans}")
"""
