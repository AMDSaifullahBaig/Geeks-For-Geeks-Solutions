from collections import Counter
class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        if len(s)%k!=0:return False
        s=[s[i:i+k] for i in range(0,len(s),k)]
        hash=Counter(s)
        if len(hash)==1:return True
        if len(hash)==2:
            return 1 in hash.values()
        return False