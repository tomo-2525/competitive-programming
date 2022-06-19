S = [int(x) for x in input()]

flag = 0
if S[0]*len(S) == sum(S):
    flag = 1

tmp = S[0]
for i in range(len(S)-1):
    if (tmp+1)%10 != S[i+1]:
        break
    tmp += 1
    if i == len(S)-2:
        flag = 1


if flag == 1:
    print("Weak")
else:
    print("Strong")
