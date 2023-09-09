# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        result_node = ListNode()
        head = result_node
        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                head.next = ListNode(curr1.val,None)
                curr1 = curr1.next
            else:
                head.next = ListNode(curr2.val,None)
                curr2 = curr2.next
            head = head.next

        if curr1 == None:
            head.next = curr2
        else:
            head.next = curr1
        
        return result_node.next