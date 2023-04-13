#Follows two pointer approach
"""
1. Initialise i=0 and j=1
2. Start iterating through the array,
      if arr[i]==arr[j], j++
      else i++ and arr[i] = arr[j] (copy the next unique value)
3. Return i+1
"""

#Time complexity: O(n)
class Solution(object):
    def removeDuplicates(self, nums):
        i,j = 0,1
        while j<len(nums):
            if nums[i]!=nums[j]:
                i+=1
                nums[i] = nums[j]
            j+=1
            
        return i+1
