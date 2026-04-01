class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash1={}
        ans=False
        
        for i in range(len(nums)):
            if nums[i] in hash1:
                ans= True
                print(nums[i])
            else:
                hash1[nums[i]]=1
        
        return ans
            