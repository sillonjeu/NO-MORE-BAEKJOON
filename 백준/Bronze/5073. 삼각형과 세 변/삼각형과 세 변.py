import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))

    if all(item == 0 for item in arr):
        break

    arr = sorted(arr)
    
    if arr[2] >= arr[1] + arr[0]:
        print("Invalid")
    elif all(item == arr[0] for item in arr):
        print("Equilateral")
    elif arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]:
        print("Isosceles")
    else:
        print("Scalene")