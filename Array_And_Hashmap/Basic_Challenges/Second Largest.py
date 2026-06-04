class Solution:
    def getSecondLargest(self, arr):
        hash=set(arr)
        arr=list(hash)
        arr.sort()
        if len(arr)==1:return -1
        return arr[-2]