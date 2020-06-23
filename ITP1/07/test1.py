cubes = [1, 8, 27, 65, 125]
add_data = [1, 2, 3]
cubes.append(6 ** 3)
cubes.append(7 ** 3)
print(cubes)  # 出力：[1, 8, 27, 27, 125, 216, 343]

cubes.append(add_data)
print(cubes)  # 出力：[1, 8, 27, 27, 125, 216, 343]

cubes.append([1, 2, 3])
print(cubes)  # 出力：[1, 8, 27, 27, 125, 216, 343]
