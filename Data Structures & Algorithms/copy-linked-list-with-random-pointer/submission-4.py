"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #the way to solve is to first store them is:
        #one pass = first take the original node as key and copied version of original as the value in a dict
        #second pass = in this we can do both next and random pointer together
        #but we havent connected the nodes but how?(for random ,it could be the case where start node random may point to the last node)
        #in dict they are technically connected together so through virtually we can connect them
                
        if not head:
            return None

        # Pass 1: Clone all nodes and store them in the map    
        old_new = {None: None}
        curr = head
        while curr:
            old_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            clone = old_new[curr]
            clone.next = old_new[curr.next]
            clone.random = old_new[curr.random]
            curr = curr.next
        return old_new[head]