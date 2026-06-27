class Solution:
    def countWays(self, n, m):
        mod=(10**9)+7
        dp=[[0]*(m+1) for i in range(n+1)]
        def recursion(n,m):
            if dp[n][m]!=0:
                return dp[n][m]
            if n<m:
                return 1
            if n==m:
                return 2
            dp[n][m]=(recursion(n-m,m)+recursion(n-1,m))%mod
            return dp[n][m]
        return recursion(n,m)