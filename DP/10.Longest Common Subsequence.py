# TC - O(n X m)
# SC - O(n X m)

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        s1 = len(text1)
        s2 = len(text2)
        lcs = [[0 for i in range(s1+1)] for j in range(s2+1)]
        for i in range(1,s2+1):
            for j in range(1,s1+1):
                if text1[j-1]==text2[i-1]:
                    lcs[i][j] = lcs[i-1][j-1]+1
                else:
                    lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
        return lcs[s2][s1]
