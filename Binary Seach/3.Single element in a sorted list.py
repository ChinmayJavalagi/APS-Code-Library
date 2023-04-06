"""
           | 
    Ex: 1,1|2,3,3,4,4,6,6,8,8
 left-half |     right-half
      
      
1. We try to find the left half of the single element.
2. We first point the l = 0 and r = len(nums)-1 and then start iterating until l<=r.

We need to observe that in the right half, index of 1st instance of an element is odd, and the 2nd instance is even.
                   similarly in left half, index of 1st instance of an element is even, and the 2nd instance is odd.
3. Since we are find the start point of the left half, we should check whether mid of l and r and mid^1 (will be even number if mid is odd and vice versa) are same. If yes then we are in the left half, so we shrink the search space by l = mid+1. Else we shrink the right half by r = mid-1. 
"""
#TC - O(logn)
class Solution(object):
    def singleNonDuplicate(self, nums):
        
        l,r = 0,len(nums)-2
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == nums[mid^1]:
                l = mid+1
            else:
                r = mid-1
        return nums[l]
