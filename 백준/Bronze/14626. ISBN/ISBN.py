import sys

arr = list(sys.stdin.readline().strip())

result = 0
spot = 0

for index, item in enumerate(arr):
    if item == "*":
        spot = index
    else:
        if index % 2 == 0:
            result += int(item)
        else: 
            result += int(item) * 3

if spot % 2 == 0:
    print(10 - (result % 10))
else:
    count = 0
    while True:
        if (result + (count * 3)) % 10 == 0:
            break
        count += 1
    print(count)