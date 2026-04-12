# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # so we need to look at our carry always, but initially we just wanna
        # create a linked list - nothing about this having to be in place

        dummy = curr = ListNode()

        # track a carry OUTSIDE OF the loop since we're going to be developing it
        carry = 0

        # why or statements: we want to iterate through each list while EITHER
        # of them still have a digit. this is why we carry the edge cases of 
        # when l1/2 is None
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            
            if l2:
                v2 = l2.val
            else:
                v2 = 0

            # add the numbers
            value = v1 + v2 + carry
            carry = value // 10
            value = value % 10

            # insert the new list node with this value and iterate forward
            curr.next = ListNode(value)
            curr = curr.next

            # NOW, UPDATE YOUR POINTERS
            if l1:
                l1 = l1.next
            else:
                l1 = None
            
            if l2:
                l2 = l2.next
            else:
                l2 = None
            

        return dummy.next



