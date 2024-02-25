# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_zigzag = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # Solve for left 
        self.solve(root, 0, 0)

        # Solve for right
        self.solve(root, 0, 1)

        return self.max_zigzag

    def solve(self, curr, val, dir):
        if curr:
            self.max_zigzag = max(self.max_zigzag, val)

            # Direction = left
            if dir == 0:
                self.solve(curr.right, val+1, 1)
                self.solve(curr.left, 1, 0 )
            else:
                self.solve(curr.left, val+1, 0)
                self.solve(curr.right, 1, 1 )
                    

        