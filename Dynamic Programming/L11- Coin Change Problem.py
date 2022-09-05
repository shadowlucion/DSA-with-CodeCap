# Recursive Apporach 
class Solution:
    def count(self, coins, N, SUM):
     dp = {}
        def solve(n,cap):
            if cap==0:
                return 1
            elif n==0:
                return 0
            elif (n,cap) in dp:
                return dp[(n,cap)]
            else:
                val = coins[n-1]
                if val<=cap:
                    c1 = solve(n,cap-val)
                    c2 = solve(n-1,cap)
                    c = c1+c2 
                else:
                    c = solve(n-1,cap)
                dp[(n,cap)] = c 
                return c
        return solve(N,SUM)
  
  # Iterative Approach
  class Solution:
    def count(self, coins, N, SUM):
        dp = [[0]*(SUM+1) for _ in range(N+1)]
        for i in range(N+1):
            for j in range(SUM+1):
                cap = j 
                n = i 
                
                if cap==0:
                    dp[i][j] = 1 
                elif n==0:
                    dp[i][j] = 0
                else:
                    val = coins[i-1]
                    if val<=cap:
                        c1 = dp[n][cap-val]
                        c2 = dp[n-1][cap]
                        dp[i][j] = c1+c2
                    else:
                        dp[i][j] = dp[n-1][cap]
        return dp[N][SUM]
                        
                    
                    
        
       
