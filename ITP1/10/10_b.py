import math
a, b, c = map(float, input().split())
c = math.radians(c)
L = a + b + (math.sqrt(a*a + b*b - 2*a*b*math.cos(c)))
S = (a * b * math.sin(c)) / 2
H = (2*S)/a

print(f"{S}\n{L}\n{H}")
