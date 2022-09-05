Problem Link: https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

# Iterative Solution / Tabulation / Bottom-Up approach
class Solution:   
    def knapSack(self,W, wt, val, N):
        dp = [[0]*(W+1) for _ in range(N)]
        for i in range(N):
            for j in range(W+1):
                cap = j 
                cv = val[i]
                cwt = wt[i]
                if cap==0:
                    dp[i][j] = 0 
                elif i==0:
                    if cwt<=cap:
                        dp[i][j] = cv
                    else:
                        dp[i][j] = 0 
                else:
                    if cwt<=cap:
                        c1 = cv+dp[i-1][cap-cwt]
                        c2 = 0+dp[i-1][cap]
                        dp[i][j] = max(c1,c2)
                    else:
                        c1 = 0+dp[i-1][cap]
                        dp[i][j] = c1 
        return dp[N-1][W]
        
# Recursive Solution / Memoization / Top-Down Appraoch        
class Solution:
    def knapSack(self,W, wt, val, N):
        dp = {}
        def solve(n,cap):
            if n==0 or cap==0:
                return 0
            elif (n,cap) in dp:
                return dp[(n,cap)]
            else:
                cwt = wt[n-1]
                cv = val[n-1]
                if cwt<=cap:
                    c1 = cv+solve(n-1,cap-cwt)
                    c2 = solve(n-1,cap)
                    c =  max(c1,c2)
                else:
                    c =  solve(n-1,cap)
                dp[(n,cap)] = c 
                return c
        return solve(N,W)
        
# Memoization where dp is an 2-D array.   
class Solution:
    def knapSack(self,W, wt, val, N):
        dp = [[-1]*(W+1) for _ in range(N+1)]
        def solve(n,cap):
            if n==0 or cap==0:
                return 0
            elif dp[n][cap]!=-1:
                return dp[n][cap]
            else:
                cwt = wt[n-1]
                cv = val[n-1]
                if cwt<=cap:
                    c1 = cv+solve(n-1,cap-cwt)
                    c2 = solve(n-1,cap)
                    c =  max(c1,c2)
                else:
                    c =  solve(n-1,cap)
                dp[n][cap] = c 
                return c
        return solve(N,W)
