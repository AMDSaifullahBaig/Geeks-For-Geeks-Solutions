class Solution:
    def canSeatAllPeople(self, k, seats):
        n=len(seats)
        for i in range(1,n):
            if seats[i]==seats[i-1]==1:
                return False
        i=0
        for i in range(n):
            if seats[i]==0:
                l=(i==0 or seats[i-1]==0)
                r=(n-1==i or seats[i+1]==0)
                if l and r:
                    k-=1
                    seats[i]=1
                    if k<=0:return True
        return k<=0