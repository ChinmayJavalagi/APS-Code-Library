'''The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.

Dijkstra doesn’t work for Graphs with negative weights/negative cycles, Bellman-Ford works for such graphs.'''

#TC - V*E

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    
    def bellman_ford(self, V, edges, S):
        #code here
        dist = [10**8]*V
        dist[S] = 0
        for i in range(V+1):
            for u,v,w in edges:
                if dist[u]!=10**8 and dist[u]+w < dist[v]:
                    if i == V:
                        return [-1]
                    dist[v] = dist[u]+w
            
        return dist
