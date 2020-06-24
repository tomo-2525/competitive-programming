s = "aiueo12345"

print(s.startswith("aiu"))
print(s.startswith("12345"))
print(s.startswith("12345", 5))
print(s.startswith("12345", 5, 7))

print(s.endswith("345"))
print(s.endswith("123"))
print(s.endswith("12345", 5))
print(s.endswith("12345", 5, 7))
