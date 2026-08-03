# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
        
        # 2. Move 'right' n + 1 times
        # This creates a gap so that when 'right' hits None, 
        # 'left' is exactly one node BEFORE the target.
        for i in range(n + 1):
            right = right.next
            
        # 3. Slide the 'window' until 'right' falls off the end
        while right:
            left = left.next
            right = right.next
            
        # 4. Skip the target node
        left.next = left.next.next
        
        # 5. Return the actual head
        return dummy.next