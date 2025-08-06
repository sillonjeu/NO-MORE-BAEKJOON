import sys
import math

A, B, V = map(int, sys.stdin.readline().strip().split())

print(math.ceil((V - A) / (A - B)) + 1)