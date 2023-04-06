"""
Bruteforce: We start from 1 and keep checking is 1 power n is equal to m, if i**n goes > m and never becomes equal then we return -1.
Binary search: Keep l=1 and h=m, iterate until h-l becomes less than one, that mean no integer root found so return -1, else do the normal binary search.
"""

class Solution:
	def NthRoot(self, n, m):
    
		if m == 1:
		    return 1
		if n == 1:
		    return m
		l, h = 1, m
		while (h-l)>1:
		    mid = (l+h)//2
		    if mid**n == m:
		        return mid
		    elif mid**n > m:
		        h = mid
		    elif mid**n < m:
		        l = mid
		    
		    
		return -1
