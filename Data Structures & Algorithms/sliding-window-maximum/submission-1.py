from heapq import heapify,heappush,heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        h=[]
        # heapify(h)
        ans=[]
        for i in range(n):
            heappush(h,(-nums[i],i))
            if i>=k-1:
                while h[0][1]<=i-k:
                    heapq.heappop(h)
                ans.append(-h[0][0])
        return ans