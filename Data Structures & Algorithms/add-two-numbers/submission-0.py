# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        list2=[]
        curr=l1
        while(curr):
            list1.append(curr.val)
            curr=curr.next

        curr=l2
        while(curr):
            list2.append(curr.val)
            curr=curr.next
        

        list1.reverse()
        list2.reverse()
        nums1 = list(map(str, list1))
        nums2 = list(map(str, list2))

        num1="".join(nums1)
        num2="".join(nums2)

        n1=int(num1)
        n2=int(num2)
        ans=n1+n2
       
        anss=list(str(ans))
        anss.reverse()
        anss = list(map(int, anss))

        dummy=ListNode(0)
        curr = dummy
        for i, digit in enumerate(anss):
            curr.val = int(digit)
            if i < len(anss) - 1:
                curr.next = ListNode(0)
                curr = curr.next

        return dummy