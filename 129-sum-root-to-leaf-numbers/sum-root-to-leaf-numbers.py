# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root : return 0

        nums = []    

        def dfs(node, num):
            
            if not node:
                return 
            
            if node.left == None and node.right == None:
                return nums.append(num+str(node.val))

            dfs(node.left, num + str(node.val))
            dfs(node.right, num + str(node.val))

        dfs(root, "")

        result = 0
        for num in nums:
            result += int(num)

        return result
        