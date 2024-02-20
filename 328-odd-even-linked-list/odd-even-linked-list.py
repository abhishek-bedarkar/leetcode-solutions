# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
             return None

        # Set odd and even head
        odd_head = head
        even_head = even = head.next
        
        # While even head and next exists
        while even_head and even_head.next:

            #Update odd pointer
            odd_head.next = odd_head.next.next
            odd_head = odd_head.next
            # Update even pointer
            even_head.next = even_head.next.next
            even_head = even_head.next

        # attach even list to odd 
        odd_head.next = even

        return head


        


        

        