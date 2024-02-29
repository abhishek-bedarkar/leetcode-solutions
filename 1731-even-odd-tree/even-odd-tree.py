# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def __init__(self):
        self.is_even_odd = None

    def height(self, root):
        if root:
            return max(self.height(root.left), self.height(root.right)) +1
        else:
            return 0

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque()
        ht = self.height(root)
        result_list = [ [] for i in range(ht)]
        lvl = 0
        if root:
            queue.append((root, lvl))
            while queue:
                node = queue.pop()
                data = node[0]
                level = node[1]
                if data:
                    if (level%2==0 and data.val%2 == 0) or (level%2==1 and data.val%2 == 1):
                        return False

                    result_list[level].append(data.val)
                    queue.append((data.right, level +1))
                    queue.append((data.left, level +1))


        else:
            return False

 
        for i,lst in enumerate(result_list):
            if i%2 ==0:
                for j in range(0, len(lst)-1):
                    if  lst[j]>=lst[j+1]:
                        return False
            else:
                for j in range(0, len(lst)-1):
                    if lst[j] <= lst[j+1]:
                        return False
        return True


        