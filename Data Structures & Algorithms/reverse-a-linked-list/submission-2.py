# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current_node = head

        #what we are trying to do is that:
        #we are changing the direction of the list of elements within the iteration itself
        #just remember that:
        # 1)Before you break the connection to the rest of the list, you must save a reference to the next node.  
        #   If you don't, you'll lose the "tail" of your list forever and your loop will have nowhere to go.
        # 2)This is where the actual reversal happens. You are telling the current node: "Stop pointing to the person in front of you, and start pointing to the person behind you
        while current_node:
            temp_next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp_next
        return prev
