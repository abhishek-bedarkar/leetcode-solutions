# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. List approach

        # n=1
        # curr = head
        # while curr.next:
        #     n += 1
        #     curr = curr.next

        # result_list = [ [] for i in range(n//2)]
        # curr = head
        # for i in range(n//2):
        #     result_list[i].append(curr.val)
        #     curr = curr.next
        
        # for j in range(n//2,n):
        #     result_list[n-1-j].append(curr.val)
        #     curr = curr.next
        
        # print(result_list)

        # return max([sum(r) for r in result_list])


        # Reverse approach
        slow, fast = head, head
        maxVal = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        curr, prev = slow, None

        while curr:       
            curr.next, prev, curr = prev, curr, curr.next   

        
        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next

        return maxVal


        