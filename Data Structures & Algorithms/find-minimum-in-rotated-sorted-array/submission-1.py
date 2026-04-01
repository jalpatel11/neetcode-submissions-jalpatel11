class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        ans=nums[0]
        while(i<=j):
            if nums[i]<nums[j]:
                ans=min(ans,nums[i])
                break
            
            m=(i+j)//2
            ans=min(ans,nums[m])
            if nums[m]>=nums[i]:
                i=m+1
            else:
                j=m-1
        
        return ans
