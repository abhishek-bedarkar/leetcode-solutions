# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next: return head

        first,second = head, head.next
        while second.next:
            temp = second.next
            second.next = first
            if first == head:
                first.next = None
            first = second
            second = temp
        second.next = first
        if first == head:
                first.next = None

        return second



