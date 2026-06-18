class Solution:
    def minRow(self,a):
        minimum=1000
        idx=0
        m=len(a)
        n=len(a[0])
        for i in range(m-1,-1,-1):
            if minimum>=a[i].count(1):
                minimum=a[i].count(1)
                idx=i
        return idx+1