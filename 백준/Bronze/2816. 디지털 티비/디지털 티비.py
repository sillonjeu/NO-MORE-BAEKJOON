import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(input().strip())

spot_KBS1 = arr.index("KBS1")
spot_KBS2 = arr.index("KBS2")

current_cursor = 0
result = ""
while arr[0] != "KBS1" or arr[1] != "KBS2":

    if arr[current_cursor] == "KBS1" and current_cursor != 0:
        result += "4"
        temp = arr[current_cursor]
        arr[current_cursor] = arr[current_cursor - 1]
        arr[current_cursor - 1] = temp
        current_cursor -= 1
    elif arr[current_cursor] == "KBS2" and current_cursor != 1:
        result += "4"
        temp = arr[current_cursor]
        arr[current_cursor] = arr[current_cursor - 1]
        arr[current_cursor - 1] = temp
        current_cursor -= 1
    elif arr[0] != "KBS1":
        if arr[current_cursor + 1] == "KBS1":
            result += "1"
        else:
            result += "3"
            temp = arr[current_cursor]
            arr[current_cursor] = arr[current_cursor + 1]
            arr[current_cursor + 1] = temp
        current_cursor += 1
    elif arr[0] == "KBS1" and arr[1] != "KBS2":
        result += "1"
        current_cursor += 1

print(result)