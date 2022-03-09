s = input()
print(s.swapcase())


"https://note.nkmk.me/python-capitalize-lower-upper-title/"

"""
別解
n=input()
m=''
for i in range(len(n)):
    c=str(n[i])
    if(n[i].islower()):
        c=n[i].upper()
    elif(n[i].isupper()):
        c=n[i].lower()
    m+=c
print(m)
"""
