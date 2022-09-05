
# Recursive Approach
class Solution:
    def minDifference(self, arr, N):
        SUM = sum(arr)
        dp = [[0]*(SUM+1) for _ in range(N)]
        for i in range(N):
            for j in range(SUM+1):
                sm = j 
                item = arr[i]
                if i==0:
                    if sm==0 or item==sm:
                        dp[i][j] = 1 
                else:
                    if item<=sm:
                        dp[i][j] = dp[i-1][sm-item] or dp[i-1][sm]
                    else:
                        dp[i][j] = dp[i-1][j]
        ans = SUM
        for j in range(SUM+1):
            if dp[N-1][j]==1:
                dif = abs(SUM-2*j)
                ans = min(ans,dif)
        return ans


# Iterative Approach
class Solution:
    def minDifference(self, arr, N):
        SUM = sum(arr)
        dp = [[0]*(SUM+1) for _ in range(N)]
        
        for i in range(N):
            for j in range(SUM+1):
                sm = j 
                item = arr[i]
                if i==0:
                    if sm==0 or item==sm:
                        dp[i][j] = 1
                else:
                    if item<=sm:
                        c1 = dp[i-1][sm-item]
                        c2 = dp[i-1][sm]
                        dp[i][j] = c1 or c2
                    else:
                        c1 = dp[i-1][sm]
                        dp[i][j] = c1 
        ans = SUM
        for j in range(SUM+1):
            if dp[N-1][j]==1:
                ans = min(ans,abs(SUM-2*j))
        return ans
