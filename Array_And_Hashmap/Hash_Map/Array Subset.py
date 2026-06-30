from collections import Counter
class Solution:
    def isSubset(self, a, b):
        if len(b)>len(a):return False
        a=Counter(a)
        for i in b:
            if a[i]>0:
                a[i]-=1
            else:
                return False
        return True