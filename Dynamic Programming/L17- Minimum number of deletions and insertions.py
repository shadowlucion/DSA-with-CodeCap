# Recursive Approach
class Solution:
	def minOperations(self, s1, s2):
	    dp = {}
	    def lcs(s1,s2,m,n):
	        if m==0 or n==0:
	            return 0 
	        elif (m,n) in dp:
	            return dp[(m,n)]
	        else:
	            if s1[m-1]==s2[n-1]:
	                c = 1+lcs(s1,s2,m-1,n-1)
	            else:
	                c1 = lcs(s1,s2,m-1,n)
	                c2 = lcs(s1,s2,m,n-1)
	                c = max(c1,c2)
	            dp[(m,n)] = c
	            return c 
	    
	    m = len(s1)
	    n = len(s2)
	    k = lcs(s1,s2,m,n)
	    return m+n-2*k
