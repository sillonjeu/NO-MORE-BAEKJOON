# 브론즈 3 
# 2025-05-07

import sys
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

count_x = 0
count_y = 0

for x in range(0, W, M + 1):
    count_x += 1

for y in range(0, H, N + 1): 
    count_y += 1

print(count_x * count_y)