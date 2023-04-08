#TC - O(n^2)
#SC - O(n)

class Solution:
    def longestSubsequence(self,a,n):
        # code here
        lis = [1]*n
        for i in range(len(a)-1,-1,-1):
            for j in range(i+1, len(a)):
                if a[i]<a[j]:
                    lis[i] = max(lis[j]+1, lis[i])
        return max(lis)
