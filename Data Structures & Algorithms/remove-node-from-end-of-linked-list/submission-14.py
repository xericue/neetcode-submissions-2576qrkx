# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = second_dummy = head
        count = second_count = 1

        while dummy.next:
            dummy = dummy.next
            count += 1

        if n == count == 1:
            return None

        print(count)
        while second_dummy:
            if second_count == count - n:
                if second_dummy.next:
                    second_dummy.next = second_dummy.next.next
                    break
            elif second_count == count - n + 1:
                return second_dummy.next

            else:
                second_dummy = second_dummy.next
                second_count += 1


        return head