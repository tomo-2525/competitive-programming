H, W, A, B = map(int, input().split())
mod = 10**9+7
C = [1, 1]
inv = [0, 1]
Cinv = [1, 1]
for i in range(2, H+W+1):
    C.append((C[-1]*i) % mod)
    inv.append((-inv[mod % i]*(mod//i) % mod))
    Cinv.append(Cinv[-1]*inv[-1] % mod)
ans = 0
for i in range(H-A):
    a = (C[i+B-1]*C[H-1-i+W-B-1]) % mod
    a = (a*Cinv[B-1]) % mod
    a = (a*Cinv[i]) % mod
    a = (a*Cinv[W-B-1]) % mod
    a = (a*Cinv[H-i-1]) % mod
    ans += a
    ans %= mod
print(ans)

"""from scipy.special import comb
H, W, A, B = map(int, input().split())
ans = 0

for i in range(W - B+1):
    ans += comb(H - A + B + i, H-A, exact=True) * \
        comb(W - B + A - i, A, exact=True)

ans = int(ans % (10**9+7))

print(ans)
"""

"""
H, W, A, B = map(int, input().split())
C = H - A
D = W - B
p = 1000000007
 
def power(a, b): #a^b (mod p)を求める #二分累乗法を使う
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a, b//2) ** 2 % p
    else:
        return power(a, b//2) ** 2 * a % p
 
f = [1] #f[i] = i! % p
for i in range(H+W):
    f.append(f[i] * (i+1) % p)
 
I_f = [0] * (H+W+1) #I_f[i] = (i!)^(-1) % p
I_f[H+W] = power(f[H+W], p-2)
for i in reversed(range(H+W)):２２
    I_f[i] = I_f[i+1] * (i+1) % p
 
def combi(a, b): #(a+b)!/a!b! (mod p)を求める
    return f[a+b] * I_f[a] * I_f[b] % p
 
x = 0
for i in range(C):
    x = (x + combi(i, B-1) * combi(D-1, H-i-1)) % p
print(x)
"""
