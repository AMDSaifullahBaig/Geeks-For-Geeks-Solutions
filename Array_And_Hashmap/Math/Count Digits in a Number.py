import math
class Solution:
    def countDigits(self, n):
        return int(math.log10(n))+1