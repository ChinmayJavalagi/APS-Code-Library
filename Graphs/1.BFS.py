# TC - (V) + (2E) [Undirected graph]
# TC - (V) + (E)  [directed graph]


from typing import List
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        visited = [False]*len(adj)
        q = deque()
        q.append(0)
        visited[0] = True
        arr = []
        while q:
            u = q.popleft()
            arr.append(u)
            for i in adj[u]:
                if visited[i] ==False:
                    q.append(i)
                    visited[i] = True
        return arr
    


#for disconnected graph run a for loop in range of len(adj) and call func bfsOfGraph 
