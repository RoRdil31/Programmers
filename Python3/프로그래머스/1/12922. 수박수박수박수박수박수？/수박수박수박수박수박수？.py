def solution(n):
    # return '수박'*(n//2) if n%2 == 0 else '수박'*(n//2) + '수'
    str1 = '수박'*n
    return str1[:n]