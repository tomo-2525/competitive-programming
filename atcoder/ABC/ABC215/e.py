# paiza ビンゴゲーム
input_line = int(input())

l = []
for i in range(4):
    l.extend(map(int,input().split()))
l2 = [0]*16 
n = [int(input()) for i in range(input_line)]

for i in n:
    if i in l:
        l2[l.index(i)]=1

flag = 0
for i in range(4):
    tate = l2[0+i] + l2[4+i] + l2[8+i] + l2[12+i]
    yoko = l2[0+i*4] + l2[1+i*4] + l2[2+i*4] + l2[3+i*4]
    if tate == 3:
        for j,k in enumerate([l2[0+i],l2[4+i],l2[8+i],l2[12+i]]):
            if k == 0:
                print(l[j*4+i]) 
                flag = 1
    if yoko == 3:
        for j,k in enumerate([l2[0+i*4],l2[1+i*4],l2[2+i*4],l2[3+i*4]]):
            if flag == 1:
                break
            if k == 0:
                print(l[j+i*4]) 
                flag = 1
        
naname = l2[0] + l2[5] + l2[10] + l2[15]
if naname == 3:
    for j,k in enumerate([l2[0],l2[5],l2[10],l2[15]]):
        if flag == 1:
            break
        if k == 0:
            print(l[5*j]) 
            flag = 1
naname = l2[3] + l2[6] + l2[9] + l2[12]
if naname == 3:
    for j,k in enumerate(l2[3],l2[6],l2[9],l2[12]):
            if flag == 1:
                break
            if k == 0:
                print(l[3*j]) 
                flag = 1
if flag == 0:
    print('no')