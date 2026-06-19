class Solution:
    def optimalArray(self, arr):
        result=[]
        curr=0
        for i in range(len(arr)):
            if i>0:
                curr+=(arr[i]-arr[i//2])
            result.append(curr)
        return result