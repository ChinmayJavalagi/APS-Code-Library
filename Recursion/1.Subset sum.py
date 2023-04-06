#Pick-not pick approach
"""
Use recursion and pick-not pick method generate subsets, but here instead of adding the subsets to a data structure to be returned, we add the sum of those numbers in the subset.
"""
# Time Complexity: O(2^n)
# Space Complexity: O(2^n) for storing subset sums, since 2^n subsets can be generated for an array of size n.
class Solution:
	def subsetSums(self, arr, N):
		# code here
		a = []
		sum = 0
		self.helper(arr, 0, a, sum, N)
		return a
		
	def helper(self, arr, i, a, sum, N):
	    if i == N:
	        a.append(sum)
	        return
	    self.helper(arr, i+1, a, sum, N)
	    self.helper(arr, i+1, a, sum+(arr[i]), N)
