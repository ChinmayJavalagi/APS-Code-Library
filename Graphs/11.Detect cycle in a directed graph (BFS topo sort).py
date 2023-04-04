from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        cnt = 0
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
            cnt+=1
            for u in adj[s]:
                indegree[u]-=1
                if indegree[u] == 0:
                    q.append(u)
        
        return 0 if cnt==V else 1
