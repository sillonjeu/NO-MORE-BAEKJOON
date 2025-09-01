import sys

n = int(sys.stdin.readline().strip())
s = [0]

for _ in range(n):
    s.append(int(sys.stdin.readline().strip()))

if n == 1:
    print(s[1])
elif n == 2:
    print(s[1] + s[2])
else:
    dp = [0] * (n + 1)
    dp[1] = s[1]
    dp[2] = s[1] + s[2]
    dp[3] = max(s[1] + s[3], s[2] + s[3])
    for i in range(4, n + 1):
        dp[i] = max(dp[i - 2] + s[i], dp[i - 3] + s[i - 1] + s[i])
    print(dp[n])