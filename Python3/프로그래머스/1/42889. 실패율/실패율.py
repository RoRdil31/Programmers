def solution(N, stages):
    odd = {}
    l = len(stages)
    for i in range(1,N+1):
        if l != 0:
            cnt_num = stages.count(i)
            odd[i] = cnt_num / l
            l -= cnt_num
        else:
            odd[i] = 0
    answer = sorted(odd, key = lambda x:-odd[x])
    return answer #[i[0] for i in answer]