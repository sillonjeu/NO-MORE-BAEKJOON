import sys

input = sys.stdin.readline

N, K = (input().split(" "))

arr = []

for _ in range(int(N)):
    current = (input().strip().split(" ")) 
    current = [int(item) for item in current]
    arr.append(current)
    
arr = sorted(arr, key=lambda x: (-x[1], -x[2], -x[3]))

check = [K, 0, 0, 0]
rank = 1

for index, item in enumerate(arr):
    if int(item[0]) == int(K):
        print(rank)
        break
    
    if check[1] == item[1] and check[2] == item[2] and check[3] == item[3]:
        continue
    else:
        rank = index + 1