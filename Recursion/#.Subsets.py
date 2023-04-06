"""
Pick not pick method.
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = []
        b = []
        n = len(nums)
        def helper(i, a, b):
            if i == n:
                b.append(a)
                return 

            helper(i+1, a+[nums[i]], b)
            helper(i+1, a, b)
        helper(0, a, b)
        return b
