# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:


        def dfs(root, target, flag):

            # base condition

            if root == None : return 0

            count = 0

            if root.val == target: count += 1
            
            # Include case
            
            count += dfs(root.left, target-root.val, True) + dfs(root.right, target-root.val, True)
            
            # Exclude case
            if not flag:
                count += dfs(root.left, target, False) + dfs(root.right, target, False)

            return count

        return dfs(root, targetSum, False)


        