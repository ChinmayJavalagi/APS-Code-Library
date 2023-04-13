"""
1. initialize a temp_cnt and a max_cnt to 0.
2. Iterate trough the list,
      if num is 1, temp_cnt++
      else, temp_cnt = 0 and max_cnt = max of temp and max
3. return max
"""

#Time Complexity: O(N)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi, cnt = 0,0
        for num in nums:
            if num == 1:
                cnt+=1
            else:
                maxi = max(maxi,cnt)
                cnt = 0
        return maxi if maxi>=cnt else cnt 
