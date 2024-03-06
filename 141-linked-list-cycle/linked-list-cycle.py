# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head and head.next:
            slow = head
            fast = head.next
            while slow and fast.next and slow.next and fast.next.next:
                if fast == slow:
                    return True
                
                slow = slow.next
                fast = fast.next.next
        else:
            return False
        