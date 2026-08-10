# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        before = dummy

        while True:

            # Find the kth node of the current group
            cur = before
            count = 0

            while count < k:
                cur = cur.next
                count += 1

                # Fewer than k nodes remain
                if cur is None:
                    return dummy.next

            # Node after the current group
            temp = cur.next

            # First node of the current group
            start_node = before.next

            # Reverse the current group
            prev = temp
            cur1 = start_node

            while cur1 != temp:
                temp1 = cur1.next
                cur1.next = prev
                prev = cur1
                cur1 = temp1

            # Connect previous part to reversed group
            before.next = prev

            # The original first node is now the tail
            # of the reversed group
            before = start_node