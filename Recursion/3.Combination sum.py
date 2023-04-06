"""
1. Here we use some modification to the pick-not pick method.
2. While recursing, We first check if the num is less than the target,
      if yes, then we subtract the target with the num and again send the same index to check if we can use the same element again(not pick condition)
      if no, we go to the next index while keeping the target unchanged.
"""
#Time Complexity: O(2^t * k) where t is the target, k is the average length

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        ans = []
        def helper(ind, target):
            if ind == len(candidates):
                if target == 0:
                    ans.append(res[:])
                return
        
            if candidates[ind]<=target:
                res.append(candidates[ind])
                helper(ind, target-candidates[ind])
                res.pop()
            helper(ind+1, target)
        
        helper(0, target)
        return ans
