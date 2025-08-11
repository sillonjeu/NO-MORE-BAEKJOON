import sys

N = int(sys.stdin.readline().strip())

count = 0
current = 1

while count != N:
    c = str(current).find("666")

    if c != -1:
        count += 1
    current += 1

print(current - 1)