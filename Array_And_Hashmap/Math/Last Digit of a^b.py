class Solution:
    def getLastDigit(self, a: str, b: str) -> int:
        if b=="0":
            return 1
        base=int(a[-1])
        if len(b)>1:
            exp=int(b[-2:])%4
        else:
            exp=int(b)%4
        if exp==0:
            exp=4
        return (base**exp)%10