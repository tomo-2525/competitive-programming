s = "a i u e o"
print(s)  # a i u e o

l = s.split()
print(l)  # ['a', 'i', 'u', 'e', 'o']

s2 = ",".join(l)
print(s2)  # a,i,u,e,o


s = "いっぱい"
s = s.replace("い", "お")
print(s)

s = s.replace("ぱ", "")
print(s)

s = s.strip("お")
print(s)
