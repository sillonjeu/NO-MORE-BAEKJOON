import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

m = max(arr)
sum = 0

for item in arr:
    sum += (item / m) * 100

print(sum / len(arr))