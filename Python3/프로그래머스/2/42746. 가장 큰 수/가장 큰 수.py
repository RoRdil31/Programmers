def solution(numbers):
    numbers = sorted([str(n) for n in numbers], key = lambda x : x*3, reverse=True)
    
    return (''.join(numbers)).lstrip('0') if (''.join(numbers)).lstrip('0')!='' else '0'  # str(int(''.join(numbers)))

