class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        ans = []

        def helper(ind):
            if ind == len(s):
                ans.append(res[:])
                return
            for i in range(ind,len(s)):
                if s[ind:i+1] == s[ind:i+1][::-1]:
                    res.append(s[ind:i+1])
                    helper(i+1)  
                    res.pop()


        helper(0)
        print(ans)
        return ans
