import sys

while True:
    S = list(sys.stdin.readline().strip())

    if S == ["0"]:
        break

    flag = True
    for index in range(0, len(S) // 2):
        if S[index] != S[len(S)-index-1]:
            flag = False
            break
    
    if flag: 
        print("yes")
    else:
        print("no")
    