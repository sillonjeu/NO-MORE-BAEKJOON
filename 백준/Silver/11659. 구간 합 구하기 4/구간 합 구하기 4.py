import sys

N, M = map(int, (sys.stdin.readline().strip().split())) 

arr = list(sys.stdin.readline().strip().split())
arr = [int(item) for item in arr]

cal_arr = [0] * (N)
cal_arr[0] = arr[0]

for index in range(1, N):
    cal_arr[index] = cal_arr[index - 1] + arr[index]

for _ in range(M):
    start, end = map(int, (sys.stdin.readline().strip().split()))

    if start == 1:
        print(cal_arr[end - 1])
    else:
        print(cal_arr[end - 1] - cal_arr[start - 2])