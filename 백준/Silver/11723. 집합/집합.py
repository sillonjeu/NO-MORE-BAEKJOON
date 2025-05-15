import sys

input = sys.stdin.readline

M = int(input())
Set = set()

for _ in range(M):
    data = input().strip().split(" ")

    if data[0] == "add":
        Set.add(int(data[1]))
    elif data[0] == "remove":
        if int(data[1]) in Set:
            Set.remove(int(data[1]))
    elif data[0] == "check":
        if int(data[1]) in Set:
            print(1)
        else:
            print(0)
    elif data[0] == "toggle":
        if int(data[1]) in Set:
            Set.remove(int(data[1]))
        else:
            Set.add(int(data[1]))
    elif data[0] == "all":
        for item in range(1, 21):
            Set.add(item)
    elif data[0] == "empty":
        Set = set()