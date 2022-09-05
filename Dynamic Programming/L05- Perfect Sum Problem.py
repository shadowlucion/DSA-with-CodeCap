 # https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1
 
 # Recursive Solution
 class Solution:
    def perfectSum(self, arr, N, sum):
        dp = {}
        arr.sort(reverse=True)
        mod = 10**9+7
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
                    c = (c1+c2)%mod 
                else:
                    if sm==0:
                        c = 1 
                    else: 
                        c = 0
                dp[(n,sm)] = c
                return c 
        return solve(N,sum) 
        
        
# Tabulation Solution
class Solution:
    def perfectSum(self, arr, N, sum):
        dp = [[0]*(sum+1) for _ in range(N)]
        mod = 10**9+7
        for i in range(N):
            for j in range(sum+1):
                sm = j 
                item = arr[i]
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
                    item = arr[i]
                    if item<=sm:
                        dp[i][j] = (dp[i-1][sm-item]+dp[i-1][sm])%mod
                    else:
                        dp[i][j] = dp[i-1][sm]
        return dp[N-1][sum]
        
        
