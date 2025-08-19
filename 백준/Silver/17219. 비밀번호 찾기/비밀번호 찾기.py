import sys

N, M = map(int, sys.stdin.readline().strip().split())

Dict = {}
for _ in range(N):
    url, site = sys.stdin.readline().strip().split()

    Dict[url] = site

for _ in range(M):
    url = sys.stdin.readline().strip()
    print(Dict.get(url))