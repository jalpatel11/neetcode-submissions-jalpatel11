class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        j=n-1
        max1=0
        while(i<j):
            width=j-i
            h=min(heights[i],heights[j])
            prod=h*width
            if prod>max1:
                max1=prod
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return max1