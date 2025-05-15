# NO-MORE-BAEKJOON
### Starting fresh on Baekjoon — no answer sheets, no GPT, a brand new account.

![mazandi profile](http://mazandi.herokuapp.com/api?handle=sillonjeu&theme=dark)

# 구현
## 순열
```python
from itertools import permutations, combinations, product, combinations_with_replacement

# 배열, 몇 개로 만들 것인지

# 순서대로 순열, 조합, 중복 순열, 중복 조합
list(permutations(arr, 2)) 
list(combinations(arr, 2)) 
list(product(arr, repeat = 2)) 
list(combinations_with_replacement(arr, 2)) 
```

## Counter
```python
from collections import Counter(대문자임)

arr = Counter(["A", "B", "C", "A", "B"])

# 배열 안에 있는 요소들의 개수로 장난칠 때 유용함.

# 중복 제거해서 요소들 반환
print(arr.keys())
=> dict_keys(['A', 'B', 'C'])

# 각각 원소랑 원소가 몇 개 있는지 반환 
print(arr.items())
=> dict_items([('A', 2), ('B', 2), ('C', 1)])

# 최빈값을 n개 반환
print(arr.most_common(2))
=> [('A', 2), ('B', 2)]

# 특정 원소에 대해 몇 개 나왔는지 뽑아낼 수 있음
print(arr["A"])
=> 2
```

## deque
```python
from collections import deque

arr = deque(arr)

# 보통 스택/큐를 구현할 때 많이 이용한다.
# 스택에서 무작정 이거 사용하지 말고, 단순하게 변수에 1씩 늘려서 하는 방법도 생각해라.

# pop
arr.pop()
arr.popleft()

# append
arr.append()
arr.appendleft()
```

## for, while
```python
# item 활용
for item in arr

# index, item 활용
for index, item in enumerate(arr)

# 리스트 컴프리헨션
list(index for index in range(0, 10))
=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# while 돌리기
while arr:
```

## zip
```python
# 동일한 인덱스끼리 묶어서 반환
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

result = zip(names, ages)
print(list(result))
=> [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# 비교에도 유용하게 사용
def is_convertible(word1, word2):
	return sum([w1 != w2 for w1, w2 in zip(word1, word2)]) == 1
```

## reduce
```python
from functools import reduce

result = reduce(lambda x, 집계 함수, 배열, 초기값(없어도됨))

# ex) 누적합에 많이 사용함
arr = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, arr, 1)
=> 10

result = reduce(lambda x, y: x * y, arr)
=> 24
```

## sorted
```python
# 정렬
arr = sorted(arr, key=len, reverse=True)

# 복합 정렬. 괄호 꼭 붙여줘야함!!
arr = sorted(arr, key=lambda x: (-x[1][0], x[0]))

# 복합 정렬 - lambda에서 두 개의 변수가 필요할 경우 
ex) arr = [2, 6, 10]을 조합해서 가장 큰 수를 만들 것
from functools import cmp_to_key
arr = sorted(arr, key=lambda x, y: int(x + y) - int(y + x))
```

## math, 연산
```python
import math

# 제곱근
math.sqrt(7)

# 로그값
math.log(8, 2)

# 팩토리얼
math.factorial(7)

# 최대 공약수
math.gcd(35, 14)

# 최소 공배수
num = 35 * 14 // math.gcd(35, 14)

# 절대값
print(abs(-3))

# 삼항 연산자
return x if 조건문 else y

# 변환: 문자 => 아스키 정수 값
print(ord("A"))
# 변환: 숫자 => 2진수, 이거 쓰려면 앞 두 문자는 떼야함
print(bin(10))
```

## string
```python
import string

# 알파벳 리스트 만들기
alpha = list(string.ascii_uppercase)
=> ["A", "B", "C" ...]

# 알파벳인지 판별
print("A".isalpha())
=> True
```

## list
```python
arr = [1, 2, 4, 5]

# 특정 위치에 삽입
arr.insert(index, item)

# 평탄화해서 넣기
arr1.extend(arr2)

# 삭제 - 값 기준
arr.remove(item)
# 삭제 - 인덱스 기준
del arr[1]

# 조회 - 인덱스 기준
arr.index(1)

# any, all
if all(10 > item for item in arr)
if any(10 > item for item in arr)

# 배열 선언 - 1차원
arr = [0] * n
# 배열 선언 - 2차원
arr = [[0] * len(arr[0]) for _ in range(len(arr))]

# 배열 다루기
arr[start : end]
=> start는 index 기준, end는 for문 다룰때랑 똑같음
arr[:]
=> 배열 깊은 복사
arr[:-1]
=> 뒤에 한 문자 자르기

# 요소들 변환
"".join(arr)

arr = ["".join(map(str, item)) for item in arr]
=> 순열 조합으로 만들었을 때 이런식으로 조합도 가능
=> 여기서 map(str, arr)은 배열의 요소들을 문자로 변환하는 것
```

## str
```python
Str = "abCdea"

# 대문자, 소문자
Str.upper()
Str.lower()

# 변경
Str.replace("#A", "a")

# 문자 자체 판단
ch.isdigit()

# 탐색 - 값 기준
Str.find("a")
=> 0(index 값)
Str.count("a")
=> 2(등장하는 횟수)

# 겹치는 접두사
Str.startswith("ab")
=> True
```

# Dict
```python
# 선언
Dict = {"A": 1, "B": 2, "C": 3}
Dict = dict(zip(arr1, arr2))

# 생성, 추가 
Dict["A"] = 1

# 삭제
del Dict["A"]

# 조회
Dict.get("A", 0)

# 값 반환
Dict.keys()
=> dict_keys(['A', 'B', 'C'])
Dict.values()
=> dict_values([1, 2, 3])
```

# Set
```python
# 선언
Set = set()

# 삽입
Set.add("A")

# 삭제
Set.remove("A")
```

# heapq
```python
import heapq

arr = []

# 선언: O(N)
heapq.heapify(arr) 

# pop, push
heapq.heappop(arr)
heapq.heappush(arr, item)

# heapq는 최소 힙이 기본임
# 따라서 최대 힙은 음수로 값을 집어넣음
heapq.heappush(arr, -1) ...
print(-heapq.heappop(arr))
```

# 탐색
## 완전 탐색
```python
# 약수 완전탐색 할때는 math.sart(num) + 1까지 하기
for index in range(1, int(math.sqrt(cal)) + 1):
```
## 이분 탐색
### bisect
```python
from bisect import bisect_left, bisect_right

arr = [1, 2, 3, 6, 7, 8]

# 정렬된 배열에서 특정 원소의 인덱스 값을 찾을 때 유용하다.
# 각각 5를 삽입할 가장 왼쪽 인덱스, 오른쪽 인덱스
print(bisect_left(arr, 5))
print(bisect_right(arr, 5))
```
## 슬라이딩 윈도우
```python
# 단계적 갱신, 빈도 관리, 누적합을 할 때 사용되는 기법 
# O(1) ~ O(log n)
# Counter랑 조합해서 사용하기도 함

def max_sliding_window_sum(arr, K):
    window_sum = sum(arr[:K])  # 첫 윈도우 합
    max_sum = window_sum       # 일단 이것을 최댓값으로 초기화

    for i in range(len(arr) - K):
        window_sum = window_sum - arr[i] + arr[i + K]  # 윈도우 한 칸 이동
        max_sum = max(max_sum, window_sum)
        
    return max_sum

# 실행 예시
arr = [2, 7, 3, 1, 5, 2, 6, 2]
K = 3
print(max_sliding_window_sum(arr, K))  # 13
```
## BFS/DFS
```python
# BFS는 최단거리 할 때 유용. 꼭 visited를 이용하자
```
## 백트래킹
```python
# 조건을 만족하지 못하면 탐색을 조기에 종료하고 이전 단계로 되돌아가기
N = 4
board = [0] * N  # board[i]는 i번째 행에서 퀸이 놓인 열 번호를 의미
count = 0

def is_safe(row):
    for i in range(row):
        # 열 중복 또는 대각선 체크
        if board[row] == board[i] or abs(board[row] - board[i]) == row - i:
            return False
    return True

def backtracking(row):
    global count
    if row == N:
        print(board)
        count += 1
        return
    for col in range(N):
        board[row] = col
        if is_safe(row):  # 조건에 맞으면 다음 행으로 진행
            backtracking(row + 1)

backtracking(0)
print(f"해답 개수: {count}")
```

# 탐욕(그리디) 알고리즘

# Stack, Queue

# DP
```python
# 1, 2, 3... n에서 n번째 방법은 총 몇 가지수가 나오는지 구하는건 피보나치와 동일하다.
for i in range(3, n + 1):
  dp[i] = (dp[i - 1] + dp[i - 2])
        
# 가장 큰 수를 더해서 만드는 문제는 맨 끝 or 끝에서 두 번째 시점으로 되돌아가보기
# 밑의 예시는 트리
for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
```

# 누적합
```python
# 시뮬레이션 문제 풀 때 누적합도 한 번 고려해보기
def solution(book_time):
    timeline = [0] * 1501  # 0분부터 1500분까지

    for start, end in book_time:
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))

        start_min = sh * 60 + sm
        end_min = eh * 60 + em + 10  # 10분 청소시간 포함

        timeline[start_min] += 1
        timeline[end_min] -= 1

    current = 0
    result = 0
    for t in range(1501):
        current += timeline[t]
        result = max(result, current)

    return result
```

# 재귀




