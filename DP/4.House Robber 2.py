# TC - O(n)
# SC - O(1)

class Solution(object):
    def rob(self, nums):
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        rob1,rob2 = 0,0
        for n in nums:
            temp = max(n+rob1,rob2)
            rob1 = rob2 
            rob2 = temp
        return rob2
