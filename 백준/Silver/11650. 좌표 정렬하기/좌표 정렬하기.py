import sys

N = int(sys.stdin.readline().strip())

arr = []
for _ in range(N):
    x, y = sys.stdin.readline().strip().split()

    arr.append([x, y])

arr = sorted(arr, key = lambda x : (int(x[0]), int(x[1])))

for item in arr:
    print(item[0], item[1])
