class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_p = 1
        postfix_p = 1
        result = [0]*n
        for i in range(n):
            result[i] = prefix_p
            prefix_p *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= postfix_p
            postfix_p *= nums[i]
        return result