# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        q = deque([root])
        res = []
        final = []
        while q:
            lis = []
            q1 = len(q)

            for i in range(len(q)):
                node = q.popleft()
                lis.append(node.val)   # correction: node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(lis)            # move this outside the for loop

        for i in res:
            final.append(i.pop())

        return final 