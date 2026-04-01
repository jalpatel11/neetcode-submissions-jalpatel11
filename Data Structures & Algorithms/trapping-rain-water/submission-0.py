class Solution:
    def trap(self, height: List[int]) -> int:
        
        n=len(height)
        if n==0:
            return 0
        prefix_sum = [0] * n
        prefix_sum[0] = height[0]
        for i in range(1, n):
            prefix_sum[i] = max(prefix_sum[i-1], height[i])

        suffix = [0] * n
        suffix[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1],height[i])

        ans=0


        for i in range(n):
            ans+= min(prefix_sum[i],suffix[i])-height[i]
        return ans
