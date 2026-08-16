# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(node):
            result = []

            def preorder(node):
                if not node:
                    result.append(None)
                    return
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)

            preorder(node)
            return result

        root_list = serialize(root)
        sub_list = serialize(subRoot)

        for i in range(len(root_list) - len(sub_list) + 1):
            if root_list[i:i + len(sub_list)] == sub_list:
                return True

        return False