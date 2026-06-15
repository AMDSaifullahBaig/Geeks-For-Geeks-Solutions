class Solution:
    def minimumCost(self, cost, w):
        inf=float("inf")
        dp=[inf]*(w+1)
        dp[0]=0
        for i in range(1,len(cost)+1):
            price=cost[i-1]
            if price==-1:
                continue
            for j in range(i,w+1):
                if dp[j-i]!=inf:
                    dp[j]=min(dp[j],dp[j-i]+price)
        return dp[w] if dp[w]!=inf else -1