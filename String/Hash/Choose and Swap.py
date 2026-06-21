class Solution:
    def chooseSwap(self, s):
        unique=sorted(list(set(s)))
        char=set(unique)
        for i in s:
            char.discard(i)
            minimum=None
            for c in unique:
                if c in char:
                    if c<i:
                        minimum=c
                    break
            if minimum:
                result=[]
                for c in s:
                    if c==i:
                        result.append(minimum)
                    elif c==minimum:
                        result.append(i)
                    else:
                        result.append(c)
                return "".join(result)          
        return s   