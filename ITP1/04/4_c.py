# 例）入力：1 + 2
while True:
    a, op, b = input().split()
    a, b = [int(x) for x in [a, b]]
    # print(f"{type(a)}{type(op)}{type(b)}")  #<class 'int'><class 'str'><class 'int'>

    if op == "+":
        print(f"{a+b}")

    elif op == "-":
        print(f"{a-b}")

    elif op == "*":
        print(f"{a*b}")

    elif op == "/":
        print(f"{a//b}")

    else:
        break

"""
別解１
while True:
    a,op,b = input().split()
    a = int(a)
    b = int(b)
    if op == '?':
        break
    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(a//b)
"""
