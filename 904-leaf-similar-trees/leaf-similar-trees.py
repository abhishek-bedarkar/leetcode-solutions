# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result1=[]
        self.result2 =[]
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.dfs(root1,self.result1)
        self.dfs(root2,self.result2)
        print(self.result1)
        print(self.result2)
        return self.result1 == self.result2
    
    def dfs(self, root,result):

        if root:
            if root.left == None and root.right == None:
                result.append(root.val)

            else:
                self.dfs(root.left, result)
                self.dfs(root.right, result)

        