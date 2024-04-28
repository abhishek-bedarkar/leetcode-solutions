# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # base condition
        if not root:
            return root
        
        if root.val> key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:

            if not root.left:
                return root.right
            if not root.right:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left
            
            root.val = cur.val

            root.right = self.deleteNode(root.right, cur.val)
        
        return root


        