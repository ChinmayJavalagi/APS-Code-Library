class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, curNums):
            if len(nums) == 0:
                perm.append(curNums)
                return
            for i in range(len(nums)):
                cur = nums[i]
                newNums = nums[:i] + nums[i+1:]
                helper(newNums, curNums+[cur])
        
        perm = []
        helper(nums, [])
        return perm
