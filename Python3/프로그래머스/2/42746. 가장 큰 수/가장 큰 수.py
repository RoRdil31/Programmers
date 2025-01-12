def solution(numbers):
    answer = ''
    nums = [(str(i)*4,len(str(i))) for i in numbers]
    for i in sorted(nums, reverse=True): answer += i[0][:i[1]]
    
    return answer if len(answer)!=answer.count('0') else '0'



















# def solution(numbers):
#     numbers = sorted([str(n) for n in numbers], key = lambda x : x*3, reverse=True)
    
#     return (''.join(numbers)).lstrip('0') if (''.join(numbers)).lstrip('0')!='' else '0'  # str(int(''.join(numbers)))

