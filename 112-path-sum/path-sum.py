# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.found = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, curr_sum, target):
            if not self.found and root:
                curr_sum += root.val
                if curr_sum  == target and root.left == None and root.right == None:
                    self.found = True    
                else:
                    if root:
                        dfs(root.left, curr_sum, target)
                        dfs(root.right, curr_sum, target)
        
        dfs(root, 0, targetSum)
        return self.found


        