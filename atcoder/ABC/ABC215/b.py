import math 

n = int(input())
if math.pow(2,int(math.log2(n))) <= n:
    print(int(math.log2(n)))    
else:
    print(int(math.log2(n))-1)

