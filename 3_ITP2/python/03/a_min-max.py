from sys import stdin

l = list(map(int, stdin.readline().split()))
print(f'{min(l)} {max(l)}')

"""
l = list(map(int, input().split()))

print(f'{min(l)} {max(l)}')
"""