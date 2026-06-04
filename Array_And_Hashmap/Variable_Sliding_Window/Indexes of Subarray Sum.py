class Solution:
    def subarraySum(self, arr, target):
        l=0
        add=0
        for i in range(len(arr)):
            add+=arr[i]
            while add>target and l<=i:
                add-=arr[l]
                l+=1
            if add==target:
                return [l+1,i+1]
        return [-1]