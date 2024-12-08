from collections import deque
def solution(prices):
    answer = [-1]*len(prices)
    queue = deque()
    prices = deque((idx,i) for idx, i in enumerate(prices))
    queue.append(prices.popleft())
    
    while prices:
        idx, p = prices.popleft()
        if queue[-1][1] > p :
            remove_idx = []
            for q_idx, q_p in queue:
                if answer[q_idx] == -1 and q_p > p :
                    answer[q_idx] = idx - q_idx    
                    remove_idx.append(q_idx)
            queue = deque(item for item in queue if item[0] not in remove_idx)
        queue.append((idx,p))
        
    length = len(answer)
    answer = [(length-1-idx) if i==-1 else i for idx, i in enumerate(answer)]
    
    return answer