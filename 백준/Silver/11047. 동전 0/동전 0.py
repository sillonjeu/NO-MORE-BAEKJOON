import sys

N, K = map(int, sys.stdin.readline().strip().split())

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().strip()))

arr = sorted(arr, key=lambda x: -x)

count = 0
for item in arr:
    count += (K // item)
    K %= item

print(count)