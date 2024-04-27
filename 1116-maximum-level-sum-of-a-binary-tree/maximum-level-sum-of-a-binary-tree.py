# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        max_sum = float("-inf")
        current_level, level = 0, 0
        while queue:
            current_level += 1
            level_size = len(queue)
            current_level_sum=0

            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if current_level_sum > max_sum:
                max_sum = current_level_sum
                level = current_level
            
        return level


        