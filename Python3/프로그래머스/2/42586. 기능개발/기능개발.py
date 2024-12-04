import math
def solution(progresses, speeds):
    answer = []
    prog = [math.ceil((100-i)/j) for i,j in zip(progresses, speeds)]
    maxnum, cnt = prog[0], 0
    for i in prog:
        if maxnum < i :
            maxnum = i
            answer.append(cnt)
            cnt = 1
            continue
        cnt += 1
    answer.append(cnt)
    return answer