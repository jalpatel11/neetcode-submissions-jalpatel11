class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]

        for i, num in enumerate(nums):
            ans.append([num,i])

        i=0
        j=len(nums)-1

        ans.sort()
        while(i<j):
            sum=ans[i][0]+ans[j][0]

            if sum==target:
                return [min(ans[i][1],ans[j][1]), max(ans[i][1],ans[j][1])]
            if(target>sum):
                i+=1
            else:
                j-=1
        
        return []