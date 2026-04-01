class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        inde= defaultdict()

        for i,num in enumerate(numbers):
            if target-num in inde:
                return [inde[target-num],i+1]
            inde[num]=i+1
        


