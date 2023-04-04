'''Floyd–Warshall algorithm is an algorithm for finding shortest paths in a directed weighted graph 
with positive or negative edge weights.
A single execution of the algorithm will find the lengths of shortest paths between all pairs of vertices.'''

# TC - N**3

import math
class Solution:
	def shortest_distance(self, matrix):
		#Code here
		n = len(matrix)
		for via in range(n):
    		for i in range(n):
    		    for j in range(n):
    		        if matrix[i][j] == -1:
    		            matrix[i][j] = math.inf
    		        matrix[i][j] = min(matrix[i][j], matrix[i][via]+matrix[via][j])
    	
    	for i in range(n):
    	    for j in range(n):
    	        if matrix[i][j] == math.inf:
    	            matrix[i][j] = -1
    	return matrix
