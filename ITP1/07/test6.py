gvar = 'hoge'


def testfunc():
    global gvar
    var = 1
    global var
    gvar = '0123'
    print(gvar)


print(var)
print(gvar)  # 出力：hoge
testfunc()  # 出力：0123
print(gvar)  # 出力：0123
