class Solution:
    def isBalanced(self, s):
        arr=[]
        dic={"(":")","{":"}","[":"]"}
        for i in s:
            if i in dic:
                arr.append(i)
            else:
                if arr and dic[arr[-1]]==i:
                    arr.pop()
                else:
                    return False
        return not arr