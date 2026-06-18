class Solution:
    def findCoverage(self, mat):
        if not mat or not mat[0]:
            return 0
        c=0
        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    if any(mat[k][j]==1 for k in range(0,i)):
                        c+=1
                    if any(mat[k][j]==1 for k in range(i+1,m)):
                        c+=1
                    if any(mat[i][k]==1 for k in range(0,j)):
                        c+=1
                    if any(mat[i][k]==1 for k in range(j+1,n)):
                        c+=1
        return c