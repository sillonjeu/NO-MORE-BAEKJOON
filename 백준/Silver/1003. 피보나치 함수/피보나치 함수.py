import sys

T = int(sys.stdin.readline().strip())

dp_0 = [0] * 41
dp_1 = [0] * 41

dp_0[0] = 1
dp_1[1] = 1

for index in range(2, 41):
    dp_0[index] = dp_0[index - 1] + dp_0[index - 2]
    dp_1[index] = dp_1[index - 1] + dp_1[index - 2]

for _ in range(T):
    current = int(sys.stdin.readline().strip())

    print(dp_0[current], dp_1[current])