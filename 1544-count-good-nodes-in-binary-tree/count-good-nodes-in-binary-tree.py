# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result=0

    def goodNodes(self, root: TreeNode) -> int:
        self.inorder(root, float('-inf'))
        return self.result

    def inorder(self, root, max_val):
        if root:   
            if root.val >= max_val:
                self.result += 1
            max_val = max(max_val, root.val)
            self.inorder(root.left, max_val)
            self.inorder(root.right, max_val)
        
        