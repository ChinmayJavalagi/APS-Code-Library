#Fix a number and solve it like two sum
"""
1. Sort the array.
2. Iterate from the beginning, fix nums[i], then do binary search for rest of the nums.

Note: To update the pointers during binary search, updating just one pointer is enough. So we just update the left pointer untill we skip the duplicates.
"""

#TC - 

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            l,r = i+1, len(nums)-1
            if i>0 and a == nums[i-1]:
                continue
            while l<r:
                if a+nums[l]+nums[r]<0:
                    l += 1
                elif a+nums[l]+nums[r]>0:
                    r -= 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res
