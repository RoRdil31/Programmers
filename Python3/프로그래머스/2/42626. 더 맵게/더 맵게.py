import heapq as hq
def solution(scov, K):
    cnt = 0
    hq.heapify(scov)
    
    while len(scov) > 1 and scov[0] < K:
        m1 = hq.heappop(scov)
        m2 = hq.heappop(scov)
        hq.heappush(scov, m1 + (m2*2))
        cnt += 1
    
    return cnt if scov[0] >= K else -1

















# import heapq
# def solution(sco, K):
#     cnt = 0
#     heapq.heapify(sco)
#     while len(sco) >= 2 and sco[0] < K:
#         m1 = heapq.heappop(sco)
#         m2 = heapq.heappop(sco)
#         heapq.heappush(sco, m1+m2*2)
#         cnt += 1
    
#     return cnt if sco[0]>=K else -1




















# # import heapq
# # def solution(scov, K):
# #     cnt = 0
# #     heapq.heapify(scov)
# #     while len(scov) > 1:
# #         m1 = heapq.heappop(scov)
# #         m2 = heapq.heappop(scov)
# #         if (m1 >= K) : return cnt
# #         new = m1 + m2*2
# #         heapq.heappush(scov, new)
# #         cnt += 1
        
# #     return cnt if scov[0] >= K else -1
