import sys
from collections import Counter

input = sys.stdin.readline
arr = Counter(input().strip().upper())

if len(arr.most_common(2)) <= 1:
    print(arr.most_common(1)[0][0])
elif arr.most_common(2)[0][1] == arr.most_common(2)[1][1]:
    print("?")
else: 
    print(arr.most_common(1)[0][0])