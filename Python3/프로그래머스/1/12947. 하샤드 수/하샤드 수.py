def solution(x):
    return True if ( x % sum([int(i) for i in str(x)]) ) == 0 else False























# def solution(x):
#     return x%(sum(int(i) for i in str(x)))==0