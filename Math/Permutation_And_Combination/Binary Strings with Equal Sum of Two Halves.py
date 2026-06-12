class Solution:
    def computeValue(self, n):
        mod=10**9+7
        num=1
        den=1
        for i in range(n):
            num*=2*n-i
            den*=n-i
        return num//den%mod