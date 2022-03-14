s = "あいうえおアイウエオ12345"
print(s.find("あ"))  # 0
print(s.find("あい"))  # 0
print(s.find("12"))  # 10

s = "あ　い　う　え　お　ア　イ　ウ　エ　オ　1　2　3　4　5　"
print(s.index("あ"))  # 0
print(s.index("あい"))
print(s.index("1"))  # 20
print(s.index("5", 10))  # 28
print(s.index("あ", 2, 10))  # -1
