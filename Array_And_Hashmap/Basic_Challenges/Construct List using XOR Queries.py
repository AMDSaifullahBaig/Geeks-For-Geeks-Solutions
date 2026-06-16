class Solution:
    def constructList(self, queries):
        arr=[0]
        xor=0
        for i in queries:
            if i[0]==0:
                arr.append(i[1]^xor)
            else:
                xor^=i[1]
        arr=[arr[i]^xor for i in range(len(arr))]
        arr.sort()
        return arr