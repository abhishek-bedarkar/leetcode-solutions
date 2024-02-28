# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.height = 0
        self.result = None

    def findHeight(self, root):
        if not root:
            return 0
        else:
            left = self.findHeight(root.left)
            right = self.findHeight(root.right)
            return max(left, right)+1
    
    def dfs(self, root, ht):
        if root and self.result == None:
            self.dfs(root.left, ht+1)
            if ht == self.height:
                self.result = root.val
            self.dfs(root.right, ht+1)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        self.height = self.findHeight(root)
        self.dfs(root, 1)
        return self.result

        