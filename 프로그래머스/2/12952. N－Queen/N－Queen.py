def solution(n):
    result = 0
    
    # 각 열에 퀸이 있는지 체크
    cols = [False] * n
    # 대각선 체크 (왼쪽 위 -> 오른쪽 아래)
    diag1 = [False] * (2 * n - 1)
    # 대각선 체크 (오른쪽 위 -> 왼쪽 아래)
    diag2 = [False] * (2 * n - 1)
    
    def is_safe(row, col):
        """해당 위치에 퀸을 놓을 수 있는지 확인"""
        # 같은 열에 퀸이 있는지
        if cols[col]:
            return False
        # 대각선에 퀸이 있는지
        if diag1[row + col]:
            return False
        if diag2[row - col + n - 1]:
            return False
        return True
    
    def place_queen(row, col):
        """퀸을 배치하고 체크 표시"""
        cols[col] = True
        diag1[row + col] = True
        diag2[row - col + n - 1] = True
    
    def remove_queen(row, col):
        """퀸을 제거하고 체크 해제"""
        cols[col] = False
        diag1[row + col] = False
        diag2[row - col + n - 1] = False
    
    def backtrack(row):
        """백트래킹으로 모든 가능한 배치 탐색"""
        nonlocal result
        
        # 모든 행에 퀸을 성공적으로 배치한 경우
        if row == n:
            result += 1
            return
        
        # 현재 행의 각 열을 시도
        for col in range(n):
            if is_safe(row, col):
                place_queen(row, col)  # 퀸 배치
                backtrack(row + 1)      # 다음 행으로
                remove_queen(row, col)  # 백트래킹: 퀸 제거
    
    backtrack(0)  # 0번 행부터 시작
    return result

## 코드 동작 설명

### 1. **체크 배열의 의미**
# - `cols[i]`: i번 열에 퀸이 있으면 True
# - `diag1[i]`: 왼쪽 위→오른쪽 아래 대각선 (row + col이 같으면 같은 대각선)
# - `diag2[i]`: 오른쪽 위→왼쪽 아래 대각선 (row - col이 같으면 같은 대각선)

### 2. **백트래킹 과정 (n=4 예시)**
# ```
# 행 0: (0,1)에 퀸 배치
# 행 1: (1,3)에 퀸 배치
# 행 2: (2,0)에 퀸 배치
# 행 3: (3,2)에 퀸 배치 → 성공! result++

# 되돌아가서...
# 행 3: 다른 위치 시도 → 없음
# 행 2: 다른 위치 시도 → ...