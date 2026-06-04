class Solution:
    def findDuplicates(self, arr):
        hash=set()
        result=[]
        for i in arr: 
            if i in hash:
                result.append(i)
            else:
                hash.add(i)
        return result 