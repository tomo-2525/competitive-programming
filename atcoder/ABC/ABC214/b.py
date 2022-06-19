S, T = map(int, input().split())

flag = 0
for i in range(100+1):
    for j in range(100+1):
        for k in range(100+1):
            if i+j+k <= S and i*j*k <=T:
                flag += 1
print(flag)