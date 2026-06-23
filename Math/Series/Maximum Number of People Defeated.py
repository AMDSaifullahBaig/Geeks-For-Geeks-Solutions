class Solution:
    def maxPeopleDefeated(self, p):
        l=0
        r=1.732*(10**4)
        while l<=r:
            m=l+(r-l)//2
            val=m*(m+1)*(2*m+1)//6
            if val<=p:
                result=m
                l=m+1
            else:
                r=m-1
        return int(result)