class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp=nums1+nums2
        temp.sort()
        n=len(temp)
        mid=n//2
        if n%2==0:

            return ((temp[mid]+temp[mid-1])/2)
        else:
            return temp[mid]



        