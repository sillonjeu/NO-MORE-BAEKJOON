import sys

N = int(sys.stdin.readline().strip())

arr = []

for _ in range(N):
    x, y = sys.stdin.readline().strip().split()
    
    arr.append([int(x), int(y)])

arr = sorted(arr, key=lambda x: (x[1], x[0]))

for [x, y] in arr:
    print(x, y)