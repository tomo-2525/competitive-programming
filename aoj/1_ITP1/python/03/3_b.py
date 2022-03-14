i = 1
while True:
    a = int(input())
    if a == 0:
        break
    print(f"Case {i}: {a}")
    i += 1

"""
別解１
case_num = 1

while True:
    tmp_num = int(input())
    if tmp_num == 0:
        break
    else:
        print("Case %d: %d" % (case_num,tmp_num))
        case_num += 1
"""
