class Solution:
    def minOps(self, arr):
        n=len(arr)
        total=sum(arr)
        minimum=min(arr)
        return total-(minimum*n)