def solution(arr):
    answer = [arr[0]]
    before = arr[0]
    
    for i in arr[1:]:
        if before != i:
            answer.append(i)
            before = i
            
    return answer