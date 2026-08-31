# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # We know that list is non-empty
        num1 = 0
        num2 = 0
        mult = 1
        curr1 = l1
        curr2 = l2
        while curr1:
            num1 += mult * curr1.val
            mult *= 10
            curr1 = curr1.next
        mult = 1
        while curr2:
            num2 += mult * curr2.val
            mult *= 10
            curr2 = curr2.next
        print(num1+num2)
        total = str(num1 + num2)[::-1] #Reverse to put in correct order
        res = ListNode(7) #Placeholder value while we initialize linked list
        pointer = res #We move this pointer through linked list
        for i in range(len(total)-1):
            pointer.val = total[i]
            pointer.next = ListNode(7) #Again, a placeholder
            pointer = pointer.next
        #At this point, we have the last element to insert.
        #Pointer currently points to last, since we increment with next,
        #and the last is a node with placeholder value
        # We can simply insert the last one here
        pointer.val = total[-1] #Last element
        return res








