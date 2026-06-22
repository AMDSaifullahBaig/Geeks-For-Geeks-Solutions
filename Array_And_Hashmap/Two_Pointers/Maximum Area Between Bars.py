class Solution:
    def maxArea(self, height):
        maximum=0
        l=0
        r=len(height)-1
        while l<=r:
            if height[l]>height[r]:
                maximum=max(maximum,height[r]*(r-l-1))
                r-=1
            else:
                maximum=max(maximum,height[l]*(r-l-1))
                l+=1
        return maximum    