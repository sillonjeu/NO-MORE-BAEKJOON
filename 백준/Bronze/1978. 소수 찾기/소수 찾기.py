import sys
import math

# 소수 찾기
# 소수는 sqrt 쓰면 됨
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

result = 0
for item in arr:
    
    if item == 1: continue
    if item == 2: 
        result += 1
        continue

    flag = True
    for num in range(2, math.floor(math.sqrt(item)) + 1):
        if item % num == 0:
            flag = False
            break
    if flag:
        result += 1 

print(result)
