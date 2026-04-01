class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm={}
        ans=[]
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]]+=1
            else:
                hm[nums[i]]=1

        sorted_dict_asc = sorted(hm.items(), key=lambda item: item[1],reverse=True)
        print(sorted_dict_asc)

        first_k_keys = [item[0] for item in sorted_dict_asc[:k]]
        return  first_k_keys

    
            

