contacts = {'Taro': 1234, 'Jiro': 4321}
keys = list(contacts.keys())  # list()を使うことに注意
print(keys)  # 出力：['Taro', 'Jiro']

contacts = {'Taro': 1234, 'Jiro': 4321}
values = list(contacts.values())  # list()を使うことに注意
print(values)  # 出力：[1234, 4321]

contacts = {'Taro': 1234, 'Jiro': 4321}
print(contacts)  # 出力：{'Taro': 1234, 'Jiro': 4321}
items = list(contacts.items())  # list()を使うことに注意
print(items)  # [('Taro', 1234), ('Jiro', 4321)]


contacts = {'Taro': 1234, 'Jiro': 4321}
del contacts["Taro"]
print(contacts)  # {'Jiro': 4321}

print(items[1])
items[0][0] = 1111
print(items)
