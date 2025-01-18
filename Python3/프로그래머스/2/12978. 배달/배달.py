import heapq as hq
def solution(N, road, K):
    ways = {i:[] for i in range(1,N+1)}
    road = sorted(road, key=lambda x:x[0])
    for r in road:
        x,y,v= r
        ways[x].append([y,v])
        ways[y].append([x,v])
    
    def Dijkstra(start):
        nodes = {i:500001 for i in ways}
        nodes[start] = 0
        queue = [(start, 0)]
        
        while queue:
            c_node, c_dist = hq.heappop(queue)
            if c_dist > K : continue
            
            for neigh, dist in ways[c_node]:
                n_dist = c_dist + dist
                if n_dist < nodes[neigh]: 
                    nodes[neigh] = n_dist
                    hq.heappush(queue,(neigh, n_dist))
        return nodes
        
    nodes = Dijkstra(1)
    
    return sum(1 for n,v in nodes.items() if v <= K)