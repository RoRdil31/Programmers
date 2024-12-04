from itertools import permutations
def solution(k, dungeons):
    max_cnt = 0
    for perm in permutations(dungeons):
        cnt, k2 = 0, k
        for i,j in perm:
            if k2 >= i : k2 -= j; cnt += 1
        if cnt > max_cnt : max_cnt = cnt
        
    return max_cnt