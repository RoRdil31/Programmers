def solution(arr):
    global answer
    answer = [0,0]
    quad(arr, answer, len(arr))
    return answer
    
def quad(arr, s, l):
        x, y, tg = s[0], s[1], arr[s[0]][s[1]]
        for i in range(l):
            for j in range(l):
                if arr[x+i][y+j] != tg:
                    quad(arr, [x, y], l//2)
                    quad(arr, [x+l//2, y], l//2)
                    quad(arr, [x, y+l//2], l//2)
                    quad(arr, [x+l//2, y+l//2], l//2)
                    return
        answer[tg] += 1
        