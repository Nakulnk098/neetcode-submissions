# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = deque([root])
        res = []

        while q:
            lis = []
            q1 = len(q)

            for i in range(q1):
                node = q.popleft()
                lis.append(node.val)

                if len(lis) == q1:
                    res.append(lis)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return res

                