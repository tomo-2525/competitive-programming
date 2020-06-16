r = float(input())

print(f"{r*r*3.141592653589} {2*r*3.141592653589}")

"""
別解１
import math
r = float(input())
print("%.10f %.10f"%(r*r*math.pi,2.0*math.pi*r))

別解２
from math import pi
r = float(input())
print("{0:.6f} {1:.6f}".format(pi*r**2, 2*pi*r))
"""
