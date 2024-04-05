# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length, digit, carry = 0,0,0
        head1, head2 = l1,l2
        while l1 and l2:
            digit = l1.val + l2.val +carry
            carry =0
            if digit >= 10:
                l1.val ,l2.val = digit%10, digit%10
                carry = digit//10

            else:
                l1.val, l2.val = digit, digit

            if carry != 0 and l1.next == None and l2.next == None:
                #print(carry,' for l1')
                head2.val = carry
                l1.next = head2
                head2.next = None
                return head1

            l1 = l1.next
            l2 = l2.next

        if l1 != None or l2 != None:
            if l1:
                while l1:
                    digit = l1.val + carry
                    carry =0
                    if digit >=10:
                        l1.val = digit%10
                        carry = digit//10
                    else:
                        l1.val = digit

                    
                    if carry != 0 and l1.next == None:
                        #print(carry,' for l1')
                        head2.val = carry
                        l1.next = head2
                        head2.next = None
                        return head1

                    l1 = l1.next
                return head1
                    
            else:
                while l2:
                    digit = l2.val + carry
                    carry =0
                    if digit >=10:
                        l2.val = digit%10
                        carry = digit//10
                    else:
                        l2.val = digit
                    
                    if carry != 0 and l2.next == None:
                        #print(carry,' for l2')
                        head1.val = carry
                        l2.next = head1
                        head1.next = None
                        return head2
                    l2 = l2.next

                return head2
        
        


        return head1




        