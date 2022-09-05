# Problem Link: https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

# Tabulation Solution
class Solution:
    def isSubsetSum (self, N, arr, sum):
        dp = [[0]*(sum+1) for _ in range(N)]
        
        for i in range(N):
            for j in range(sum+1):
                sm = j
                cwt = arr[i]
                if sm==0:
                    dp[i][j] = 1 
                elif i==0:
                    if cwt==sm:
                        dp[i][j] = 1 
                    else:
                        dp[i][j] = 0 
                else:
                    if cwt<=sm:
                        dp[i][j] = dp[i-1][sm] or dp[i-1][sm-cwt]
                    else:
                        dp[i][j] = dp[i-1][sm]
       
        return dp[N-1][sum]
        
       
# Recursive Solution

class Solution:
    def isSubsetSum (self, N, arr, sum):
        arr.sort(reverse=True)
        dp = {}
        def solve(n,sm):
            if sm==0:
                return 1 
            elif n==0:
                return 0 
            elif (n,sm) in dp:
                return dp[(n,sm)]
            else:
                wt = arr[n-1]
                if wt<=sm:
                    c1 = solve(n-1,sm-wt)
                    c2 = solve(n-1,sm)
                    c = c1 or c2
                else:
                    c = 0
                dp[(n,sm)] = c
                return c
        return solve(N,sum)
