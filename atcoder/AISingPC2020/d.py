"""
def change_num(tmp, i):
    if tmp[i] == "0":
        return int(tmp, 2)+pow(2, N-i-1)
    else:
        return int(tmp, 2)-pow(2, N-i-1)


def popcount(num):
    tmp1 = bin(num)
    tmp2 = tmp1[2:]
    return tmp2.count("1")


N = int(input())
X = input()
flag = 0

for i in range(N):
    tmp = change_num(X, i)
    # num1 = str(tmp).count("1")
    num1 = popcount(tmp)
    while tmp > 0:
        # print(f"tmp={tmp},num1={num1}")
        tmp = tmp % num1
        num1 = popcount(tmp)
        flag += 1
    print(flag)
    flag = 0
"""
"""
回答例↓　自分のやつはTLE
"""
n = int(input())  # ２進数の桁数
x = input()  # 値
t = int(x, 2)  # ２進数を１０真数に直す
c = x.count('1')  # 値の１の数
a = t % -~c  # 　~はビット反転
print(c)
print(~c)
print(-~c)
print(t)
print(a)
#(変数) = (条件がTrueのときの値) if (条件) else (条件がFalseのときの値)
b = 0 if c < 2 else t % ~-c
for i in range(n):
    if int(x[i]):
        if c < 2:
            print(0)
            continue
        else:
            t = (b-pow(2, n-i-1, c-1)) % ~-c
    else:
        t = (a+pow(2, n-i-1, c+1)) % -~c
    z = 1
    while t:
        d = bin(t).count('1')
        t %= d
        z += 1
    print(z)
