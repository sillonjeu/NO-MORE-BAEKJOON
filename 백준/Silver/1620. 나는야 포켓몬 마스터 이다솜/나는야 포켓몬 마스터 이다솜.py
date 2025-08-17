import sys

N, M = map(int, sys.stdin.readline().strip().split())

Dict_P = {}
Dict_N = {}

for count in range(N):
    current = sys.stdin.readline().strip()
    Dict_P[current] = count + 1
    Dict_N[str(count + 1)] = current

for _ in range(M):
    current = sys.stdin.readline().strip()

    if Dict_P.get(current, 0) != 0:
        print(Dict_P.get(current))
    
    else:
        print(Dict_N.get(current)) 