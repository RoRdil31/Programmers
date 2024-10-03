import numpy as np
def solution(arr1, arr2):
    answer = np.array(arr1)+np.array(arr2)
    return answer.tolist()


def solution(arr1, arr2):
    answer = []
    
    for i,j in zip(arr1, arr2):
        sum = []
        for n,m in zip(i,j):
            sum.append(n+m)
        answer.append(sum)
    
    return answer
