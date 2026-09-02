# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([(root, root.val)])
        count = 1

        while q:
            node, q1 = q.popleft()

            if node.left:
                if node.left.val >= q1:
                    count += 1
                q.append((node.left, max(q1, node.left.val)))

            if node.right:
                if node.right.val >= q1:
                    count += 1
                q.append((node.right, max(q1, node.right.val)))

        return count

