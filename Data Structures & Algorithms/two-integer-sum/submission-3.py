class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}

        for i, num in enumerate(nums):
            dif= target-num
            if dif in ans:
                return[ans[dif],i]
            ans[num]=i