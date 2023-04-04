'''A Spanning Tree is a tree which have V vertices and V-1 edges. All nodes in a spanning tree are reachable from each other.


A Minimum Spanning Tree - the least cost path that goes through the entire graph and touches every vertex.

Necessary conditions for Minimum Spanning Tree:

It must not form a cycle i.e, no edge is traversed twice.
There must be no other spanning tree with lesser weight.

"Intiution -> Greedy" 
'''

# TC - E*log(E)


import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        pq = []
        
        #[weight, node]
        heapq.heappush(pq, [0,0])
        sum = 0
        visited = [0]*V
        
        while pq:
            s = heapq.heappop(pq)
            
            w = s[0]
            n = s[1]
            
            if visited[n] == 1:
                continue
            visited[n] = 1
            sum += w
            
            #given -> adj[0] = node
            #adj[1] = weight
            for u in adj[n]:
                adjNode = u[0]
                edW = u[1]
                if not visited[adjNode]:
                    heapq.heappush(pq, [edW, adjNode])
                    
        return sum
