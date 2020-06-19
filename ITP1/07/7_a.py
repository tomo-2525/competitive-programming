while True:
    m, r, f = map(int, input().split())
    grade = "null"

    if m == -1 and r == -1 and f == -1:
        break

    if m + r >= 80:
        grade = "A"
    elif m + r >= 65 and m + r < 80:
        grade = "B"
    elif m + r >= 50 and m + r < 65:
        grade = "C"
    elif m + r >= 30 and m + r < 50:
        grade = "D"
    elif m + r <= 30:
        grade = "F"

    if grade == "D" and f >= 50:
        grade = "C"

    if m == -1 or r == -1:
        grade = "F"

    print(grade)
