# TC - O(n)
# SC - O(1)

class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        curmax,curmin = 1,1
        for n in nums:
            if n == 0:
                curmax,curmin = 1,1
                continue
            temp = curmax*n
            curmax = max(n*curmax,n*curmin,n)
            curmin = min(temp,curmin*n,n)
            res = max(res,curmax)
        return res
