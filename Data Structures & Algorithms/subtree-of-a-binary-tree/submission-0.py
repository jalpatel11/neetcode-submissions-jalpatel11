# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not q or not p:
            return False

        queue1=deque([p])
        queue2=deque([q])

        while queue1:
            node1=queue1.popleft()
            node2=queue2.popleft()

            if node1.val!=node2.val:
                return False

            if bool(node1.left) != bool(node2.left):
                return False
            if node1.left and node2.left:
                queue1.append(node1.left)
                queue2.append(node2.left) 

            if bool(node1.right) != bool(node2.right):
                return False

            if node1.right and node2.right:
                queue1.append(node1.right)
                queue2.append(node2.right)

       
        return True