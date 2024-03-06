# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkVal(self, root, val):
        if not root:
            return root

        if root.val == val:
            return root
        elif root.val < val:
            return self.checkVal(root.right, val)
        else:
            return self.checkVal(root.left, val)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        else:
            return self.checkVal(root, val)
        