import sys

N = int(sys.stdin.readline().strip())

arr = []
for _ in range(N):
    s = sys.stdin.readline().strip()

    arr.append(s)

arr = list(set(arr))

arr = sorted(arr, key = lambda x: (len(x), x))

for item in arr:
    print(item)