N, L = map(int, input().split())
nols = list(map(str, input().split()))

for i in range(10*N):
    pri = N + i
    pri = str(pri)
    if any(x in pri for x in nols):
        continue
    else:
        print(pri)
        break

"""
n, k = map(int, input().split())
arr = list(map(int, input().split()))
 
while True:
    check = True
    for x in arr:
        if str(x) in str(n):
            check = False
    if check:
        break
    n += 1
print(n)
"""


"""
N,K=map(int,input().split())
out=N
N=str(N)
a = list(map(int, input().split()))
while 1<2:
    N1=N
    i=0
    for i in range(len(a)):
        if str(a[i]) in N:
            N=int(N) 
            N+=1
            N=str(N)
    if N1==N:
        break
 
print(N)
"""

"""
import math
N, K = map(int, input().split())
l = list(map(int, input().split()))
num = [i for i in range(10)]

for i in l:
    num.remove(i)
# print(num)

keta = int(math.log10(N))
digit = int(10**keta)
ans = 0
flag = 0
while ans <= N:
    if num[0] == 0:
        ans += digit * num[1]
        digit /= 10
        for i in range(keta):
            ans += digit * num[0]
            digit /= 10

    if num[0] != 0:
        ans += digit * num[0]
        digit /= 10
        for i in range(keta):
            ans += digit * num[0]
            digit /= 10
    flag += 1
print(int(ans))
"""
