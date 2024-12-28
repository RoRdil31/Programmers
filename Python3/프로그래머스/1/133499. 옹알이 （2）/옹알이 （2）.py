from collections import deque
def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    cant = ["ayaaya", "yeye", "woowoo", "mama"]
    cnt = 0
    for word in babbling:
        no_skip = True
        for x in cant: 
            if x in word : no_skip=False; break
            
        if no_skip:
            queue = deque()
            word = deque(word)
            while word:
                queue.append(word.popleft())
                if ''.join(queue) in can : queue.clear()
            if not queue : cnt += 1
    
    return cnt
























# def solution(babbling):
#     can_s = ['aya','ye','woo','ma']
#     cant_s = ['ayaaya','yeye','woowoo','mama']
#     cnt = 0
    
#     for word in babbling:
        
#         for i in cant_s : 
#             if i in word : word = word.replace(i,'x')
        
#         for i in can_s : 
#             if i in word : word = word.replace(i,' ')
        
#         word = word.replace(' ','')
        
#         if word == '' : cnt += 1
        
#     return cnt