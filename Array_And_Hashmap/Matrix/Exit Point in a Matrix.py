class Solution:
    def exitPoint(self, mat):
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        c=0
        m=len(mat)
        n=len(mat[0])
        i,j=0,0
        while 0<=i<m and 0<=j<n:
            if mat[i][j]==1:
                c=(c+1)%4
                mat[i][j]=0
            i+=dir[c][0]
            j+=dir[c][1]
        return [i-dir[c][0],j-dir[c][1]]