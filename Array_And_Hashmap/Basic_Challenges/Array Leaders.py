class Solution:
    def leaders(self, arr):
        n=len(arr)
        result=[]
        maximum=arr[n-1]
        for i in range(n-1,-1,-1):
            if arr[i]>=maximum:
                result.append(arr[i])
                maximum=arr[i]
        return result[::-1]