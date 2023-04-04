'''It finds the shortest paths from a single source vertex to all other vertices in a graph.'''

#TC - E*log(V) 

import heapq
import math
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        pq = []
        dist = [math.inf]*V
        dist[S] = 0
        heapq.heappush(pq, (0, S))
        while pq:
            s = heapq.heappop(pq)
            n = s[1]
            w = s[0]
            for i in adj[n]:
                u = i[1]
                if i[0]+w < dist[u]:
                    dist[u] = i[0]+w
                    heapq.heappush(pq, (dist[u], u))
                    
        return dist
