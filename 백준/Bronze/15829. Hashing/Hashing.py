import sys
import string
import math

alpha = list(string.ascii_lowercase)
L = int(sys.stdin.readline().strip())
arr = list(sys.stdin.readline().strip())

result = 0
for index, item in enumerate(arr):
    result += (alpha.index(item) + 1) * math.pow(31, index)

print(int(result % 1234567891))