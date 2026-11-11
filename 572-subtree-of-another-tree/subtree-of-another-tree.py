# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def sametree(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val!= q.val:
                return False

            return sametree(p.left,q.left) and sametree(p.right,q.right)
        
        def subtree(root):
            if not root:
                return False
            
            if sametree(root,subRoot):
                return True

            return subtree(root.left) or subtree(root.right)

        return subtree(root)