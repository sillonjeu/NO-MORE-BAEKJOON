import sys

N = int(sys.stdin.readline().strip())

arr = []

for index in range(0, N):
    age, name = sys.stdin.readline().strip().split()

    arr.append([index, age, name])

arr = sorted(arr, key=lambda x: (int(x[1]), int(x[0])))

for item in arr:
    print(item[1] + " " + item[2])