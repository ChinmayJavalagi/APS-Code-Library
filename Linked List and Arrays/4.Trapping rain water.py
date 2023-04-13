"""
1. Assign two pointers l=0 and r = n-1
2. Taking another two pointer to maintain maxLeft and maxRight and assign them to height[l] and height[r] respectively.
3. Init a variable res, iterate from first,
      if maxLeft is greater than maxRight, move the l pointer and store     maxleft and add maxLeft-height[l] to res.
      if not then do the same for right.
4. Return res
"""

#Time Complexity: O(N) 

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0

        l,r = 0,len(height)-1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        while l<r:
            if maxLeft<maxRight:
                l+=1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                res+= maxRight - height[r]
        return res
