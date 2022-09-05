# Recursive Approach-1
class Solution:
    def cutRod(self, price, N):
       dp = {}
        def solve(cl,rl):
            if cl==0 or rl==0:
                return 0
            elif (cl,rl) in dp:
                return dp[(cl,rl)]
            else:
                val = price[cl-1]
                if cl<=rl:
                    c1 = val+solve(cl,rl-cl)
                    c2 = solve(cl-1,rl)
                    c = max(c1,c2)
                else:
                    c = solve(cl-1,rl)
                dp[(cl,rl)] = c 
                return c
        return solve(N,N)
 
 # Iterative Approach-1 
 class Solution:
    def cutRod(self, price, N):
      dp = [[0]*(N+1) for _ in range(N+1)]
        for i in range(N+1):
            for j in range(N+1):
                cl = i 
                rl = j 
                if cl==0 or rl==0:
                    dp[i][j] = 0 
                else:
                    val = price[cl-1]
                    if cl<=rl:
                        c1 = val+dp[cl][rl-cl]
                        c2 = dp[cl-1][rl]
                        dp[i][j] = max(c1,c2)
                    else:
                        dp[i][j] = dp[cl-1][rl]
        return dp[N][N]
        
# Recursive Optimized Solution
class Solution:
    def cutRod(self, price, N):
        dp = {}   
        def solve(rl):
            if rl==0:
                return 0 
            elif rl in dp:
                return dp[rl]
            else:
                ans = 0 
                for cl in range(1,rl+1):
                    ans = max(ans,price[cl-1]+solve(rl-cl))
                dp[rl] = ans
                return ans
        return solve(N)
        
# Iterative Optimized Solution
class Solution:
    def cutRod(self, price, N):
        dp = [0]*(N+1)
        for rl in range(1,N+1):
            ans = 0 
            for cl in range(1,rl+1):
                ans = max(ans,price[cl-1]+dp[rl-cl])
            dp[rl] = ans
        return dp[N]
