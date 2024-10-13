def solution(wallet, bill):
    cnt = 0
    max_w, min_w = max(wallet), min(wallet)
    # max_b, min_b = max(bill), min(bill)
    # max_w, max_b = max(wallet), max(bill)
    while max_w < max(bill) or min(bill) > min_w :
        bill[bill.index(max(bill))] = max(bill)//2
        cnt += 1
    
    return cnt