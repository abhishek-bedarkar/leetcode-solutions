# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.max_d = 0

    def height(self, root):
        if not root:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) +1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 1. Brute force approach
        # self.dfs(root)
        # return self.max_d-2

        # 2. height optimization 
        if root == None:
            return 0
        else:
            op1 = self.diameterOfBinaryTree(root.right)
            op2 = self.diameterOfBinaryTree(root.left)
            op3 = self.height(root.left) + self.height(root.right)
            return max(op1, op2, op3)

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