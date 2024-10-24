import numpy as np
def solution(board, moves):
    answer = 0
    stack = []
    board = np.array(board).T
    board = (board).tolist()
    board = [[i for i in row if i!=0] for row in board] # 0(인형없음) 제거.
    
    for m in moves:
        if board[m-1] : 
            stack.append(board[m-1].pop(0)) # stack에 인형 넣고 board[m-1]에서 해당 인형 제거.
        
        if len(stack)>=2 and stack[-1]==stack[-2] :
            answer += 2
            stack.pop()
            stack.pop()
    
    
    return answer