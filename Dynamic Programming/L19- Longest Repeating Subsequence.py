# Recursive Approach
class Solution:
	def LongestRepeatingSubsequence(self, str):
	    dp = {}
		def lcs(s1,s2,n,m):
		    if n==0 or m==0:
		        return 0 
		    elif (n,m) in dp:
		        return dp[(n,m)]
		    else:
		        if s1[n-1]==s2[m-1] and n!=m:
		            c = 1+lcs(s1,s2,n-1,m-1)
		        else:
		            c1 = lcs(s1,s2,n-1,m)
		            c2 = lcs(s1,s2,n,m-1)
		            c = max(c1,c2)
		        dp[(n,m)] = c 
		        return c
		        
		return lcs(str,str,len(str),len(str))   
