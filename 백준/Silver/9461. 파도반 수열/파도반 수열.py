import sys

T = int(sys.stdin.readline().strip())

arr = [0] * 102
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2

for current in range(5, 102): 
    arr[current] = arr[current - 1] + arr[current - 5]

for _ in range(T):
    current = int(sys.stdin.readline().strip())

    print(arr[current])
    

# 1 1 1 (1+1) 2 (1+2)3 (1+3)4 (1+4)5 7 9 12 16 