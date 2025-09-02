import sys
from collections import deque

# 컴퓨터 수, 연결된 컴퓨터 쌍의 수
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

arr = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr[x].append(y)
    arr[y].append(x)

bfs = [1]
visited[1] = True
deque(bfs)

while bfs:
    current = bfs.pop()

    for friend in arr[current]:
        if visited[friend] == False:
            visited[friend] = True
            bfs.append(friend)
            count += 1

print(count)