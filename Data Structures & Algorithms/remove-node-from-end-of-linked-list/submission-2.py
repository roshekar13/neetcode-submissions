# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        steps = count - n
        if steps == 0:
            return head.next
        
        curr = head
        for i in range(count-1):
            if (i + 1) == steps:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head

        