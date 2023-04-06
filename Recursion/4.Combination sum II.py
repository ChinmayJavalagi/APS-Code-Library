#Method 1
"""
1. Same as combination sum I problem with slight modification so that we don't repeat the elements and don't add the duplicate combinations to the result.
2. We sort the array
3. We do the same stuff as the previous problem.
4. We first check if the num is less than the target,
      if yes, then we subtract the target with the num and INCREASE THE INDEX to ensure we don't use same element again(not pick condition)
      if no, before we go to the next index while keeping the target unchanged, we eleminate the duplicates using a while loop as the array is sorted.
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        ans = []
        candidates.sort()
        def helper(ind, target):
            if ind == len(candidates):
                if target == 0:
                    ans.append(res[:])
                return
        
            if candidates[ind]<=target:
                res.append(candidates[ind])
                helper(ind+1, target-candidates[ind])
                res.pop()
            while ind+1<len(candidates) and candidates[ind] == candidates[ind+1]:
                ind+=1
            helper(ind+1, target)
        
        helper(0, target)
        return ans
      
      

#Method 2

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        ans = []
        candidates.sort()
        def helper(ind, target):
            if target == 0:
                ans.append(res[:])
                return
            
            for i in range(ind, len(candidates)):
                if i>ind and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                res.append(candidates[i])
                helper(i+1, target-candidates[i])
                res.pop()
        
        helper(0, target)
        return ans
