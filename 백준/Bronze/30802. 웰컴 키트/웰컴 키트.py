import sys

# 티셔츠 6가지, T장 묶음으로만 주문 가능
# 펜은 1가지, P자루 묶음 or 1자루 주문 가능
# 티셔츠는 남아도 되지만, 펜은 정확히 준비되어야 함

# 그래서 티셔츠는 T장씩 최소 몇 묶음, 펜은 P자루 최대 몇 묶음 그리고 한 자루 씩 몇개 주문하는지?

# N: 참가자 수 
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
T, P = map(int, sys.stdin.readline().strip().split()) 

result_t = 0
for item in arr:
    result_t += (item // T)
    if (item % T > 0):
        result_t += 1

print(result_t)
print(N // P, N % P)