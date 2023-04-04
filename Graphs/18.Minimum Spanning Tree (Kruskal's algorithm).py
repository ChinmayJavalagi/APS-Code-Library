'''Kruskal's algorithm finds a minimum spanning forest of an undirected edge-weighted graph. If the graph is connected, it finds a minimum spanning tree. It is a greedy algorithm in graph theory as in each step it adds the next lowest-weight edge that will not form a cycle to the minimum spanning forest'''


'''
1.Sort all the edges in non-decreasing order of their weight. 
2.Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If the cycle is not formed, include this edge. Else, discard it. 
3.Repeat step#2 until there are (V-1) edges in the spanning tree.
'''
#Step #2 uses the Union-Find algorithm to detect cycles.
# TC - E*log(E) or E*log(V)

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    
    def find(self, x, parent):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent[x], parent)
        return parent[x]
    
    def union(self, x, y, parent, rank):
        x_rep = self.find(x, parent)
        y_rep = self.find(y, parent)
        
        if x_rep == y_rep:
            return
        
        if rank[x_rep] < rank[y_rep]:
            parent[x_rep] = y_rep
        elif rank[y_rep] < rank[x_rep]:
            parent[y_rep] = x_rep
        else:
            parent[y_rep] = x_rep
            rank[x_rep] +=1
        
    def spanningTree(self, V, adj):
        #code here
        edges = []
        sum = 0
        
        parent = [i for i in range(V)]
        rank = [0 for i in range(V)]
        for i in range(V):
            for j in adj[i]:
                v = i
                u = j[0]
                w = j[1]
                
                edges.append([w,u,v])
        
        edges.sort()
        for i in range(len(edges)):
            if self.find(edges[i][1], parent) == self.find(edges[i][2], parent):
                continue
            else:
                self.union(edges[i][1], edges[i][2], parent, rank)
                sum += edges[i][0]
                
        return sum
