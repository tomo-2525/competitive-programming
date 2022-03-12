n = int(input())
A = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    b, m, e = map(int, input().split())
    _A = list(A)
    for k in range(e-b):
        _A[b+(k+(e-m))%(e-b)] = A[b+k]
    A = _A
            
print(*A)



n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
	b, m, e = map(int, input().split())
	s = a[b:e]
	a = a[:b] + s[m-b:] + s[:m-b] + a[e:]
print(*a)
