'''Topological sorting for Directed Acyclic Graph (DAG) 
is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering.

Note: Topological Sorting for a graph is not possible if the graph is not a DAG.'''


# For DAG
# TC - ( V + E ) [same as dfs]

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        arr = []
        visited = [0]*V
        for i in range(V):
            if not visited[i]:
              self.dfs(adj, visited, i, arr)
        arr.reverse()
        return arr
        
        
    def dfs(self, adj, visited, s, arr):
        visited[s] = 1
        for u in adj[s]:
            if not visited[u]:
                self.dfs(adj, visited, u, arr)
        arr.append(s)
        return arr
