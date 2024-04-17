# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        result = []

        def dfs(node, chars):

            if node:

                # base condition
                if node.left == None and node.right == None:
                    result.append(chr(node.val+97)+chars)
                else:
                    dfs(node.left, chr(node.val+97)+chars)
                    dfs(node.right, chr(node.val+97)+chars)
        

        dfs(root, "")

        result.sort()

        return result[0]


        



        