#Just like Bipartite graph problem but instead of 2 colors we have m colors to check
"""
1. We initialise a color array of length V with 0's.
2. Inside the solve function, we run a loop to try all the colors, if the node of the graph can be colored or not(isSafe).
      If yes then store the color in the color array and move to the next node++, and if that call returns true(when we reach the last node+1), then return true.
      else, backtrack by again making the color array as 0.
"""

# Time Complexity: O(N**M)


def isSafe(graph, node, color, col, N):
    for k in range(N):
        if k!=node and graph[k][node] == 1 and color[k] == col:
            return False
    return True
            
def solve(node, color, m, N, graph):
    if node == N:
        return True
    for i in range(1, m+1):
        if isSafe(graph, node, color, i, N):
            color[node] = i
            if solve(node+1, color, m, N, graph):
                return True
            color[node] = 0
    return False


def graphColoring(graph, k, V):
    color = [0]*V
    if solve(0, color, k, V, graph): return True
    return False
