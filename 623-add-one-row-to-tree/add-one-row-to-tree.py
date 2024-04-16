# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        q= []
        q.append((root,1))

        # solve for depth 1
        if depth == 1:
            node = TreeNode(val, root, None)
            return node
    

        while q:
            node,height = q.pop()

            if height < depth-1:
                if node.left:
                    q.append((node.left, height+1))
                if node.right:
                    q.append((node.right, height+1))
            else:
                node.left = TreeNode(val, node.left, None)
                node.right  = TreeNode(val, None , node.right)
        return root



        