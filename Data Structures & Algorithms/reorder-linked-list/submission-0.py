# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Reordering second half
        slow = head
        fast = head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        tail = slow.next
        slow.next = None

        prev = None
        curr = tail
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #second half now reordered

        tail = prev
        front = head

        while tail:
            temp1 = front.next
            temp2 = tail.next
            front.next = tail
            tail.next = temp1
            front = temp1
            tail = temp2

        return

        