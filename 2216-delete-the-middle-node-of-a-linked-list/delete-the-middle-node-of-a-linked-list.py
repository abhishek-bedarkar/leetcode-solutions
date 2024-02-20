# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        count,mid=1,0
        curr = head
        while curr.next:
            curr = curr.next
            count +=1
        
        mid = count//2
        #print("Mid index : ", mid)
        curr = head
        while mid !=1:
            curr = curr.next
            mid -= 1
        #print("value to be deleted ", curr.next.val)
        curr.next = curr.next.next

        return head
        
        

        