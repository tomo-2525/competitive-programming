a, b, c = map(int, input().split())

if (a < b) and (b < c):
    print("Yes")
else:
    print("No")

"""
別解１
li = list(map(int, input().split()))
if li[0] < li[1] < li[2]:
    print("Yes")
else:
    print("No")

別解２    
a,b,c=map(int,input().split())
print("Yes"*(a<b<c)or"No")
"""
