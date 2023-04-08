#TC - O(n^2)
#SC - O(1)

class Solution:
    def longestPalindrome(self, S):
      
        res = ''
        for i in range(len(S)):
            
            #if odd substring
            l = i
            r = i 
            while l>=0 and r<len(S) and S[l] == S[r]:
                if len(res) < len(S[l:r+1]):
                    res = S[l:r+1]
                l -= 1
                r += 1
                
            #if even substring
            l = i
            r = i+1
            while l>=0 and r<len(S) and S[l] == S[r]:
                if len(res) < len(S[l:r+1]):
                    res = S[l:r+1]
                l -= 1
                r += 1
        
        return res
                
