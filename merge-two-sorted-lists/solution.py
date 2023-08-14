# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp=[]
        while l1 != None:
            temp.append(l1.val)
            l1 = l1.next
        while l2 != None :
            temp.append(l2.val)
            l2 = l2.next
        temp.sort()    
        result = ListNode()
        if len(temp) == 0:
            return None 
        result.val = temp[0]
        result.next = None 
        curr = result
        for i in range(1,len(temp)):
            t = ListNode()
            t.val = temp[i]
            t.next= None
            curr.next = t
            curr = curr.next
            
        return result