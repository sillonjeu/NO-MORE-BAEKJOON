import sys

while(True):
    input = list(map(int, sys.stdin.readline().strip().split()))

    if (input[0] == 0): break

    input.sort()

    if (input[0] * input[0] + input[1] * input[1] == input[2] * input[2]):
        print("right")
    else:
        print("wrong")