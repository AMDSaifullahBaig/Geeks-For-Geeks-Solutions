class Solution:
	def countWays(self, n, m):
		if n<m:return 1
		if n==m:return 2
		mod=(10**9)+7
		dp=[0]*(n+1)
		dp[0]=1
		for i in range(n+1):
			if i<m:
				dp[i]=1
			elif i==m:
				dp[i]=2
			else:
				dp[i]=(dp[i-m]+dp[i-1])%mod
		return dp[n]