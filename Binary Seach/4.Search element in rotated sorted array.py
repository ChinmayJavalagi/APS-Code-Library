'''
Array will be divided into sorted left half and right half.(observation)
and our target lies in either left or right half.
1. find mid, and check if low to mid is sorted or not if yes see is there a possibility of finding target in there.
2. If no then for sure we know that mid to high is sorted and check is there a possibility of finding target in there.
3. if yes l = mid+1 if no h = mid-1
'''
# TC - O(logn)
# SC - O(1)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return mid
            if nums[l]<=nums[mid]:
                if target<=nums[mid] and target>=nums[l]:
                    r = mid-1
                else:
                    l = mid+1

            else:
                if target>=nums[mid] and target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
