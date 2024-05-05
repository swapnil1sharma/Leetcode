# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        l = []

        def fun(x) :
            if not x :
                return 
            fun(x.left)
            l.append(x.val)
            fun(x.right)

        fun(root)
        return l
        