import sys
from collections import deque

n = int(sys.stdin.readline().strip())
arr = [0] * 12    

for num in range(12):
    count = 0
    stack = [[]]

    while stack:
        comb = stack.pop()
        s = sum(comb)

        if s == num:
            count += 1
            continue

        if s + 1 <= num: stack.append(comb + [1])
        if s + 2 <= num: stack.append(comb + [2])
        if s + 3 <= num: stack.append(comb + [3])

    arr[num] = count

for _ in range(n):
    current = int(sys.stdin.readline().strip())
    print(arr[current])