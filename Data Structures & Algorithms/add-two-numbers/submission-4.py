# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2
        carry = 0
        dummy = ListNode(0) #place holder for the final list
        curr = dummy
        # the reason we use carry in while is cause we should make sure that the last carry shouldnt miss out lets say 9 + 9 is 18 here if we just procced 8 as the final we cant cause we will miss 1 here , so thats why we do while loop 
        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            total = val1 + val2 + carry
    
            carry = total // 10
            digit = total % 10
    
            curr.next = ListNode(digit)
            curr = curr.next
    
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
        return dummy.next
