time = int(input())

print(f"{int(time/3600)}:{int((time%3600)/60)}:{time%60}")


"""
別解１
S = int(input())
print("%d:%d:%d"%(S/3600,(S%3600)/60,S%60))

別解２
sec = int(input())
print(sec//3600, ':', (sec%3600)//60, ':', sec%60, sep='')
"""