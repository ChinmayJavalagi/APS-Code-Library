"""
#Median is the middle value after combining both the arrays(if total is odd then one median, if even then middle1+middle2//2).
1. So the basic idea here is to divide the total length into half, ex: 13//2 = 6 so 7th element becomes our median.
2. l1 = [1,2,3,4,5,6,7,8] and l2 = [1,2,3,4,5]
so merged list should be [1,1,2,2,3,3,4,4,5,5,6,7,8] and median should be 4.

3. Instead of apply binary search to both the arrays we apply on just one array and the remaining we will take from another array.
4. So we always consider the array with min no elements, so if n1>n2 then swap.
5. Applying binary search to arr1 gives some mid index so that half-mid gives me no of ele in arr2.
6. In the above example 1,2,3 from l1 and 1,2,3 from l2 (l1 and l2 after swapping) will be our left half elements. We have to check if max of left half is less than max of right half (for the left half whatever we selected to be true). So we those l1 l2 and r1 r2.
"""

#TC - O(log(min(n,m)))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        total = len(nums1) + len(nums2)
        half = total//2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l, r = 0, len(nums1) - 1
        
        while True:
            cut1 = (l+r)//2
            cut2 = half-cut1-2

            l1 = nums1[cut1] if cut1>=0 else float("-infinity")
            r1 = nums1[cut1+1] if (cut1+1)<len(nums1) else float("infinity")
            l2 = nums2[cut2] if cut2>=0 else float("-infinity")
            r2 = nums2[cut2+1] if (cut2+1)<len(nums2) else float("infinity")

            if l1<=r2 and l2<=r1:
                if total%2:
                    return min(r1,r2)
                return (max(l1,l2)+min(r1,r2))/2.0
                
            elif l1>r2:
                r = cut1 - 1
            else:
                l = cut1 + 1
