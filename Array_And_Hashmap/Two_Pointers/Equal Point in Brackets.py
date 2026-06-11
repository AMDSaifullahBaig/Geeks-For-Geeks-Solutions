class Solution:
    def findIndex(self, s):
        n=len(s)
        r_count=s.count(")")
        l_count=0
        for i in range(n+1):
            if l_count==r_count:
                return i
            if s[i]=="(":
                l_count+=1
            else:
                r_count-=1
        return n-1