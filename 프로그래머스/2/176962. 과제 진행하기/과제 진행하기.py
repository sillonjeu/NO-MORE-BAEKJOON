# 시작 시간: 10:35 ~
# 풀이 방법: stack?
from collections import deque
def solution(plans):
    
    task_stack = deque([])
    arr = []
    result = []
    
    for item in plans:
        h, m = item[1].split(":")
        start = int(h) * 60 + int(m)
        
        arr.append([item[0], start, int(item[2])])
    
    arr = sorted(arr, key=lambda x: int(x[1]))
    
    for index in range(len(arr) - 1):
        start = arr[index][1]
        next_task = arr[index + 1][1]
        remain_time = arr[index + 1][1] - arr[index][1]
        
        # 다음에 할 시간보다 끝낼 수 있으면
        if start + arr[index][2] <= next_task:
            result.append(arr[index][0])
            remain_time -= arr[index][2]
            # 다 했는데 시간이 다음 시간까지 시간이 남는다면
            while remain_time > 0 and len(task_stack) > 0:
                current = task_stack.pop()
                if remain_time >= current[2]:
                    print(current, remain_time)
                    result.append(current[0])
                    remain_time -= current[2]
                else:
                    task_stack.append([current[0], current[1], current[2] - remain_time])
                    remain_time = 0
            
        # 중간에 끊긴다면
        elif start + arr[index][2] > next_task:
            arr[index][2] -= (next_task - start)
            task_stack.append([arr[index][0], arr[index][1], arr[index][2]])
            
    result.append(arr[-1][0])
    
    while len(task_stack) > 0:
        result.append(task_stack.pop()[0])
    
    return result