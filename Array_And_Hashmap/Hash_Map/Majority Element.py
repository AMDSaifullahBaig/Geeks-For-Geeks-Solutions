from collections import Counter
class Solution:
    def majorityElement(self, arr):
        n=len(arr)/2
        c=Counter(arr)
        for i in c:
            if c[i]>n:return i
        return -1