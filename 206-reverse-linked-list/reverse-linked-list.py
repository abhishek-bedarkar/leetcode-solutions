# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return head

        fr = head.next
        curr = head
        curr.next = None
        
        while fr.next:
            temp = fr.next
            fr.next = curr
            curr = fr
            fr = temp

        fr.next =curr
        return fr




        