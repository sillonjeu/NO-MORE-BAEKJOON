def solution(n, info):
    result = [-1]
    MAX = -1

    def BT(arr, count, spot):
        nonlocal result, MAX

        # 마지막 칸에 남은 화살 전부 넣기
        if spot == len(info) - 1:
            arr.append(count)       
            BT(arr, 0, spot + 1)
            arr.pop()
            return

        if spot == len(info):
            Lion = 0
            Pich = 0
            for i in range(len(info)):
                if arr[i] > info[i]:
                    Lion += (10 - i)
                elif info[i] != 0:     
                    Pich += (10 - i)

            if Lion > Pich and Lion - Pich > MAX:
                MAX = Lion - Pich
                result = arr[:]
            elif Lion > Pich and Lion - Pich == MAX:
                # 낮은 점수(뒤 인덱스)부터 비교
                better = False
                for i in range(len(arr) - 1, -1, -1):
                    if arr[i] > result[i]:
                        better = True
                        break
                    elif arr[i] < result[i]:
                        break
                if better:
                    result = arr[:]
            return

        # 선택 1) 이 과녁에 쏠 수 있으면 쏜다
        if info[spot] < count:
            arr.append(info[spot] + 1)
            BT(arr, count - (info[spot] + 1), spot + 1)
            arr.pop()

        # 선택 2) 이 과녁엔 0발
        arr.append(0)
        BT(arr, count, spot + 1)
        arr.pop()

    BT([], n, 0)
    return result
