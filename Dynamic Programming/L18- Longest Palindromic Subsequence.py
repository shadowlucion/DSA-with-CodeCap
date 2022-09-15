# Iterative Approach
class Solution:
    def longestPalinSubseq(self, S):
        s1 = S 
        s2 = S[::-1]
        n = len(s1)
        m = len(s2)
        
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
