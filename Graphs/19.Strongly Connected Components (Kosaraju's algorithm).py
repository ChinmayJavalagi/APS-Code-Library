'''Kosaraju's Algorithm is a linear time algorithm to find the strongly connected components of a directed graph

A graph is said to be strongly connected if every vertex is reachable from every other vertex.
'''

# TC - O(V+E)


from collections import defaultdict
class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        visited = [0]*V
        arr = []
        cnt = 0
        for i in range(V):                                               # TC - O(V+E)
            if not visited[i]:
                self.dfs(adj, arr, i, visited)
    
        
        adjT = defaultdict(list) 
        for i in range(V):                                                # TC - O(V+E)
            for u in adj[i]:
                adjT[u].append(i)
        
        visited = [0]*V
        while arr:
            i = arr.pop()
            if not visited[i]:
                cnt+=1
                self.dfs2(adjT, i, visited)                                # TC - O(V+E)
                
        return cnt
        
    def dfs(self, adj, arr, s, visited):
        visited[s] = 1
        for u in adj[s]:
            if not visited[u]:
                self.dfs(adj, arr, u, visited)
            
        arr.append(s)
        
    def dfs2(self, adj, s, visited):
        visited[s] = 1
        for u in adj[s]:
            if not visited[u]:
                self.dfs2(adj, u, visited)
            
