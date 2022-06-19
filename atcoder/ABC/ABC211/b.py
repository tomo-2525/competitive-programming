flags = [0] * 4

for i in range(4):
    s = input()
    if s == 'H': flags[0] = 1
    elif s== '2B' : flags[1] = 1
    elif s == '3B' : flags[2] = 1
    else: flags[3] = 1

if 0 in flags:
    print('No')
else: print('Yes')