# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next # start of second half

        # okay, so now we need to reverse this second half. let's do it iteratively
        predecessor = None

        while second_half: # because predecessor will point to our new head
            successor = second_half.next
            second_half.next = predecessor
            predecessor = second_half
            second_half = successor

        # now this is literally just merging two lists, not even sorted! :D
        first_head = head
        second_list_new_head = predecessor
        
        while second_list_new_head:
            temp_one = first_head.next
            temp_two = second_list_new_head.next
            first_head.next = second_list_new_head
            second_list_new_head.next = temp_one

            first_head = temp_one
            second_list_new_head = temp_two

        first_head.next = None
