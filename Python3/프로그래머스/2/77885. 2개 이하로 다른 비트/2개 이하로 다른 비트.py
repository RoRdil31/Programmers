def solution(numbers): # XOR
    return [((num ^ (num+1)) >> 2) + num + 1 for num in numbers]
    