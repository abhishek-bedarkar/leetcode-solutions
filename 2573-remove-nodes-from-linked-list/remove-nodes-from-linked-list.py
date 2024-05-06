# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        node = head
        
        # Create stack with monotonically decreasing values
        while node:
            if not stack:
                stack.append(head.val)
            else:
                while stack and stack[-1] < node.val:
                    stack.pop()
                
                stack.append(node.val)
            #print(f'stack : {stack}')
            node = node.next

        # Create updated linked list
        node = head
        if not stack:
            return None
        else:
            for i, elm in enumerate(stack):
                node.val = elm
                if i == len(stack)-1:
                    node.next = None
                else:
                    node = node.next
        
        return head