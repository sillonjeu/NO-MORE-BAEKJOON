# 1 (0)
# 2 ~ 7 (6-1)
# 8 ~ 19 (12-1)
# 20 ~ 37 (18-1)
# 38 ~ 61 (24-1)
# ... 반복

import sys
input = sys.stdin.readline
N = int(input())

count = 0 # 6의 배수만큼 늘어남
current = 2 # 현재 위치
result = 1 # 정답
while True:
    if N == 1:
        print(result)
        break

    if current + count - 1 >= N >= current:
        print(result)
        break

    current += (count)
    count += 6
    result += 1