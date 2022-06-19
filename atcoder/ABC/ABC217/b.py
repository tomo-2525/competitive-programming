flags = [0]*4
for i in range(3):
    s = input()
    if s[1] == 'B':
        flags[0] = 1
    elif s[1] == 'R':
        flags[1] = 1
    elif s[1] == 'G':
        flags[2] = 1
    else:
        flags[3] = 1


if flags[0] == 0:
    print('ABC')
elif flags[1] == 0:
    print('ARC')
elif flags[2] == 0:
    print('AGC')
elif flags[3] == 0:
    print('AHC')