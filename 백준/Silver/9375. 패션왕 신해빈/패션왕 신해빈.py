import sys
from collections import deque

n = int(sys.stdin.readline().strip())

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    dict = {}

    for _ in range(num):
        name, type = map(str, sys.stdin.readline().strip().split())
        dict[type] = dict.get(type, 0) + 1

    count = 1
    for item in dict.values():
        count = count * (item + 1)
    print(count - 1)