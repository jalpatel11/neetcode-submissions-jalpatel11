class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}

        for i in range(len(nums)):
         for j in range(i+1,len(nums)):
             ans[(i,j)]=nums[i]+nums[j]

        for i in ans:
             if ans[i]==target:
                 return [i[0],i[1]]