# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.list_length= 0
    def findLength(self, head):
        while head:
            self.list_length += 1
            head = head.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.findLength(head)
        pos = self.list_length  - n
        temp = head
        while pos > 1 and temp:
            temp = temp.next
            pos -=1
        
        if n ==  0:
            temp.next = None
        elif n == self.list_length:
            temp = head.next
            return temp
        elif temp != None:
            temp.next = temp.next.next
        return head
        

        