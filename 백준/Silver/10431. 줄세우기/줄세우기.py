import sys

input = sys.stdin.readline

P = int(input())

for _ in range(P):
    tk = list(input().strip().split(" "))
    tk = [int(item) for item in tk]
    arr = []
    result = 0

    for step in range(1, 21):
        for index, item in enumerate(arr):
            if tk[step] < item:
                result += len(arr) - index
                # print(step, tk[step], len(arr) - index)
                break
        arr.append(tk[step])
        arr = sorted(arr)
        # print(arr)
    
    print(_ + 1, result)


