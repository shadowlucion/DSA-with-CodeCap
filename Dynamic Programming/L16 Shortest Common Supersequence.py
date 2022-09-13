# Iterative approach.
class Solution:
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    pass 
                else:
                    if X[i-1]==Y[j-1]:
                        dp[i][j] = 1+ dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        lcs = dp[m][n]
        ans = m+n-lcs
        return ans
