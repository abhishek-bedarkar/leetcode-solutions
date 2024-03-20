# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        start, end = list1, list1

        while a-1:
            start = start.next
            a -= 1
        
        while b:
            end = end.next
            b -= 1

        list2_end = list2

        while list2_end.next:
            list2_end = list2_end.next
        
        #print(end.val)
        start.next = list2

        #print(list2_end.val)
        list2_end.next = end.next

        return list1


        
        