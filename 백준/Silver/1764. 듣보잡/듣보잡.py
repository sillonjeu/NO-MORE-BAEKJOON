import sys

N, M = map(int, sys.stdin.readline().strip().split())

Dict = {}

for _ in range(N + M):
    current = sys.stdin.readline().strip()

    Dict[current] = Dict.get(current, 0) + 1

arr = []
for item in Dict:
    if Dict[item] == 2: 
        arr.append(item)

arr.sort()

print(len(arr))
for item in arr:
    print(item)