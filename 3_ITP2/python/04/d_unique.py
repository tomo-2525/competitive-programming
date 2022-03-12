n = int(input())
a = list(map(int, input().split()))
print(*sorted(list(set(a))))