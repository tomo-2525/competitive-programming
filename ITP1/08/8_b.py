while True:
    s = str(input())
    if(s[0] == '0'):
        break
    print(sum(int(num) for num in (s)))


"""
別解    
readline = open(0).readline
write = open(1, 'w').write
while 1:
    x = readline()
    if x == "0\n":
        break
    write("%d\n" % sum(map(int, x.strip())))
"""
