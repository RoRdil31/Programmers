import heapq as hq
def solution(N, road, K):
    ways = {i:[] for i in range(1,N+1)}
    for u,v,w in road:
        ways[u].append((v,w))
        ways[v].append((u,w))
        
    def Dijkstra(start):
        nodes = {i:500001 for i in ways}
        nodes[start] = 0
        queue = [(start, 0)]
        
        while queue:
            c_node, c_dist = hq.heappop(queue)
            if c_dist > K : continue
            
            for neigh, dist in ways[c_node]:
                next_dist = dist + c_dist
                if next_dist < nodes[neigh]:
                    nodes[neigh] = next_dist
                    hq.heappush(queue, (neigh, next_dist))
                    
        return nodes
        
    result = Dijkstra(1)
    
    return sum(1 for i in result.values() if i <= K)