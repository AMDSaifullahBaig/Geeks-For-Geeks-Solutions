class Solution:
    def missingNum(self, arr):
        add=0
        for i in arr:
            add+=i
        n=len(arr)
        total=(n+2)*(n+1)/2
        return int(total-add)