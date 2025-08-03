import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().strip().split())

arr = list(map(int, sys.stdin.readline().strip().split()))

result = list(combinations(arr, 3))

num = 0
for item in result: 
    if sum(item) == M:
        num = M
        break

    if sum(item) > num and sum(item) < M:
        num = sum(item)

print(num)