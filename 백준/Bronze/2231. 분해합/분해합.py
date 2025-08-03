import sys

N = int(sys.stdin.readline())
arr = [0] * 1000001

for num in range(1, 1000000):

    cal = num + sum(map(int, list(str(num))))

    if cal > 1000000:
        continue
    
    if arr[cal] == 0: 
        arr[cal] = num

print(arr[N])
