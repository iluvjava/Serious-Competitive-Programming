#  Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def InOrderTraverse(root): 
            if root is None: 
                return None
            LeftResult = InOrderTraverse(root.left)
            if LeftResult is not None: 
                return LeftResult
            if root.val > p.val: 
                return root
            RightResults = InOrderTraverse(root.right)
            return RightResults
                    
        return InOrderTraverse(root)