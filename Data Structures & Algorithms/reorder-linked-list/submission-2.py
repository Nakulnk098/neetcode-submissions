# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #this is done so that we can get the slow to the middle 
        #we just do while fast cause then we get to know that fast has reached the wall and we can stop it 
        #from this we get two list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        #here we take the second list and reverse it just like the first problem 
        #then we are ready to perform task where we connect both the list
        prev = None
        curr = second_half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #we get to head and prev the beginning of both the list
        #we do t1 and t2 so that we dont lose the link of both the list
        #re do that again
        first, second = head, prev
        while second:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2
