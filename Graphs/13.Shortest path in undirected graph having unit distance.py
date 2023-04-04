from collections import defaultdict, deque
import math
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        dist = [math.inf]*n
        
        q = deque()
        q.append(src)
        dist[src] = 0
        while q:
            s = q.popleft()
            for i in adj[s]:
                if dist[s]+1<dist[i]:
                    dist[i] = 1+dist[s]
                    q.append(i)
                    
        for i in range(n):
            if dist[i] == math.inf:
                dist[i] = -1
        return dist
