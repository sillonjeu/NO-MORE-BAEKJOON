import sys

# 1, 5, 15, 35, 55 .. 
# 1, 4, 10, 20, 35 ..
# 1, 3, 6, 10, 15 ..
# 1, 2, 3, 4, 5 ..

# 0층 i번째는 i + 1
# i층 1번째는 1

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    # DP 테이블 초기화 (0층은 호수대로 초기화)
    dp = [[0] * (n+1) for _ in range(k+1)]

    for i in range(1, n+1):
        dp[0][i] = i

    for floor in range(1, k+1):
        dp[floor][1] = 1  # 각 층의 1호는 1
        for room in range(2, n+1):
            dp[floor][room] = dp[floor-1][room] + dp[floor][room-1]

    print(dp[k][n])