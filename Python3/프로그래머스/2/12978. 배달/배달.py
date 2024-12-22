import heapq as hq
def solution(N, road, K):
    ways = {i:[] for i in range(1,N+1)}
    for u,v,w in road:
        ways[u].append((v,w))
        ways[v].append((u,w))
        
    def dijkstra(start):
        nodes = {i:500001 for i in ways}
        nodes[start] = 0
        queue = [(0, start)]
        while queue:
            c_distance, c_node = hq.heappop(queue)
            print(c_distance, c_node)
            
            if c_distance > nodes[c_node]: continue
            
            for neighbor, weight in ways[c_node]:
                d = c_distance + weight
                if d < nodes[neighbor]:
                    nodes[neighbor] = d
                    hq.heappush(queue, (d, neighbor))
            
        return nodes
    
    
    nodes = dijkstra(1)
    
    return sum(1 for i in nodes.values() if i <= K)