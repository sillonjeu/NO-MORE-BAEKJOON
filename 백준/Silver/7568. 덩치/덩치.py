import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(input().strip().split())
for index, item in enumerate(arr):
    arr[index] = [int(inner_item) for inner_item in item]

result = []
for item in arr:
    current = 1
    for inner_item in arr:
        if item[0] < inner_item[0] and item[1] < inner_item[1]: 
            current += 1
    result.append(current)

print(*result, sep=" ")
