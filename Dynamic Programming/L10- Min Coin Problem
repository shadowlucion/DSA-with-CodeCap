# Recursive Aporach -1 
class Solution:
	def MinCoin(self, arr, amount):	
    N = len(arr)
    dp = {}
		def solve(n,amt):
		    if amt==0:
		        return 0 
		    elif n==0:
		        return float('INF')
		    elif (n,amt) in dp:
		        return dp[(n,amt)]
		    else:
		        val = arr[n-1]
		        if val<=amt:
		            c1 = 1+solve(n,amt-val)
		            c2 = solve(n-1,amt)
		            c = min(c1,c2)
		        else:
		            c = float('INF')
		        dp[(n,amt)] = c 
		        return c 
    val =  solve(N,amount)
    if val>=10**9+7:
      return -1 
    else:
      return val


# Recursive Approach-2 (Optimized space)
class Solution:
	def MinCoin(self, arr, amount):	    
		N = len(arr)
		arr.sort()
		dp = {}
		def solve(amt):
		    if amt==0:
		        return 0
		    elif amt in dp:
		        return dp[amt]
		    else:
		        ans = float('INF')
		        for coin in arr:
		            if coin<=amt:
		                ans = min(ans,1+solve(amt-coin))
		            else:
		                break 
		        dp[amt] = ans 
		        return ans
		        
		val =  solve(amount)
    if val>=10**9+7:
        return -1 
    else:
        return val


# Iterative Apporach-2 (Optimized space)
class Solution:
	def MinCoin(self, arr, amount):
	    arr.sort()
      dp = [0]*(amount+1)	    
	    for amt in range(1,amount+1):
	        ans = float('INF')
		    for coin in arr:
		        if coin<=amt:
		            ans = min(ans,1+dp[amt-coin])
		        else:
		            break 
		    dp[amt] = ans 
  
        if dp[amount]>=10**9+7:
            return -1 
        else:
            return dp[amount]
		                	
	        
