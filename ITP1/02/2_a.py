a, b = map(int, input().split())

if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a == b")

"""
別解１
a,b = map(int,input().split())

if a > b:
    op = '>'
elif a < b:
    op = '<'
else:
    op = '=='

print("a %s b"%op)


別解２
a,b=map(int,input().split());print("a "+[["==","<"][a<b],">"][a>b]+" b")
"""
