'''Finding the shortest path to a vertex is easy if you already know the shortest paths to all the vertices that can precede it. Finding the longest path to a vertex in DAG is easy if you already know the longest path to all the vertices that can precede it. 

Processing the vertices in topological order ensures that by the time you get to a vertex, you've already processed all the vertices that can precede it.

Dijkstra's algorithm is necessary for graphs that can contain cycles, because they can't be topologically sorted.'''



# TC - (V + E)

from collections import defaultdict
from typing import List
import math
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        visited = [0]*n
        adj=defaultdict(list)

        #prepare adj list 
        for u,v,w in edges:
            adj[u].append([v,w])
        arr = []
        
        #use toposort to get the linear arrangment
        for i in range(n):
            if not visited[i]:
                self.dfs(edges, visited, i, arr, adj)
                
        #calculating distance 
        dist = [math.inf]*n
        dist[0] = 0
        while arr:
            s = arr.pop()
            for i in adj[s]:
                v = i[0]
                w = i[1]
                dist[v] = min(w+dist[s], dist[v])
            
        #if the vertex is unreachable    
        for i in range(n):
            if dist[i] == math.inf:
                dist[i] = -1
        
        return dist
        

    def dfs(self, edges, visited, s, arr, adj):
        visited[s] = 1
        for u in adj[s]:
            if not visited[u[0]]:
                self.dfs(edges, visited, u[0], arr, adj)
        arr.append(s)
