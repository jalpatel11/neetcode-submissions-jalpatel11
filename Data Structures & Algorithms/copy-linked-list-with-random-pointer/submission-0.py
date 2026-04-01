"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oTc = collections.defaultdict(lambda: Node(0))
        oTc[None] = None

        cur = head
        while cur:
            oTc[cur].val = cur.val
            oTc[cur].next =    oTc[cur.next]
            oTc[cur].random =  oTc[cur.random]
            cur = cur.next
        return  oTc[head]
