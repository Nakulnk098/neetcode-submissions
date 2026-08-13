# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:          # <-- changed
            return head

        dummy = ListNode(0)        # <-- changed
        dummy.next = head          # <-- changed

        cur = dummy                # <-- changed
        begin = 0                  # <-- changed

        original_left = left       # <-- changed

        while begin < left - 1:
            cur = cur.next
            begin += 1

        start_node = cur.next
        before = cur

        cur1 = start_node
        while left < right:
            cur1 = cur1.next
            left += 1

        after = cur1.next
        reversed_tail = start_node

        cur2 = start_node
        prev = None                # <-- changed

        while cur2 != after:
            temp = cur2.next
            cur2.next = prev
            prev = cur2
            cur2 = temp

        reversed_head = prev

        before.next = reversed_head
        reversed_tail.next = after

        if original_left == 1:     # <-- changed
            return dummy.next
        else:
            return head