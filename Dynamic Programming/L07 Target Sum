# Iterative Approach
class Solution:
    def findTargetSumWays(self, arr, N, target):
        SUM = sum(arr)
        x = SUM+target 
        if x%2!=0:
            return 0 
        else:
            x = x//2 
            
        dp = [[0]*(x+1) for _ in range(N)]
        for i in range(N):
            for j in range(x+1):
                item = arr[i]
                sm = j 
                if i==0:
                    if sm==0:
                        if item==0:
                            dp[i][j] = 2 
                        else:
                            dp[i][j] = 1 
                    else:
                        if item==sm:
                            dp[i][j] = 1
                else:
                    if item<=sm:
                        dp[i][j] = dp[i-1][sm-item]+dp[i-1][sm]
                    else:
                        dp[i][j] = dp[i-1][sm]
            
        return dp[N-1][x]    

# Recursive Approach
class Solution:
  def findTargetSumWays(self, arr, N, target):
        SUM = sum(arr)
        x = SUM+target 
        if x%2!=0:
            return 0 
        else:
            x = x//2 
        dp = {}
        arr.sort(reverse=True)
        def solve(n,sm):
            if n==0:
                if sm==0:
                    return 1
                else:
                    return 0
            elif (n,sm) in dp:
                return dp[(n,sm)]
            else:
                item = arr[n-1]
                if item<=sm:
                    c1 = solve(n-1,sm-item)
                    c2 = solve(n-1,sm)
                    c = c1+c2
                else:
                    if sm==0:
                        c = 1 
                    else:
                        c = 0
                dp[(n,sm)] = c
                return c

        return solve(N,x)
