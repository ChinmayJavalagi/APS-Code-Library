from collections import deque

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        arr = []
        indegree = [0]*V
        for i in range(V):
            for u in adj[i]:
                indegree[u]+=1
        
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
                
                
        while q:
            s = q.popleft()
            arr.append(s)
            for u in adj[s]:
                indegree[u]-=1
                if indegree[u] == 0:
                    q.append(u)
                    
        return arr
