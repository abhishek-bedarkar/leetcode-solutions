# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.max_d = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_d-2

    def solve(self, root):

        if root == None:
            return 0

        return max(1+ self.solve(root.left), 1+ self.solve(root.right))

    def dfs(self, root):
        if root:
            self.dfs(root.left)
            ld = 1+self.solve(root.left)
            rd = 1+self.solve(root.right)
            cd = ld+rd
            self.max_d = max(self.max_d, cd)
            print(root.val," -> ", self.max_d)
            self.dfs(root.right)