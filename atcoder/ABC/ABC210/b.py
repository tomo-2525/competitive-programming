N = int(input())

S = [x for x in str(input())]

if S.index('1') %2 == 0:
    print('Takahashi')
else:
    print('Aoki')