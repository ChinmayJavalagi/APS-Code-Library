"""
1. Use pick-not pick method to generate all subsets. But here we should eliminate the duplicates.
2. So we first sort the array.
3. Duplicates will appear only in not picking condition. so before applying non picking condition, we eliminate the duplicate numbers as the array is sorted. We use a while loop to do the same.
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = []
        b = []
        n = len(nums)
        nums.sort()
        def helper(i, a, b):
            if i == n:
                b.append(a)
                return 

            helper(i+1, a+[nums[i]], b)
            while i+1<n and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, a, b)
        helper(0, a, b)
        return b
