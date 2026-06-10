class Solution:
    def binarySearchable(self, arr):
        def binary(l,r,n):
            while l<=r:
                m=(l+r)//2
                if arr[m]==n:return 1
                elif arr[m]>n:
                    r=m-1
                else:
                    l=m+1
            return 0
        n=len(arr)-1
        c=0
        for i in arr:
            c+=binary(0,n,i)
        return c