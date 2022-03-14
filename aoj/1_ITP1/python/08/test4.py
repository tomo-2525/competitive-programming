a = set('abracadabra')
print('a:', a)  # a: {'c', 'r', 'd', 'b', 'a'}

b = set('alacazam')
print('b:', b)  # b: {'m', 'l', 'c', 'z', 'a'}

c = a | b  #
print(c)  # {'a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'}

c = a - b  #
print(c)  # {'b', 'd', 'r'}

c = a & b
print(c)  # {'a', 'c'}

c = a ^ b
print(c)  # {'b', 'd', 'l', 'm', 'r', 'z'}
