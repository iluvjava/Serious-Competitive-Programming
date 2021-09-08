from typing import * 

"""
# Definition for a Node.

"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Edge case 
        if root is None or root.left is None: 
            return root 
        # Base case, construct the first layer correct
        root.left.next = root.right
        # Recursive case, use the previous later to link the next layer. 
        Parent = root.left
        LeftMost = Parent # left most of the previous layer. 
        while LeftMost.left is not None:
            while Parent is not None: 
                Left = Parent.left 
                Right = Parent.right
                Left.next = Right
                if Parent.next is not None:
                    Right.next = Parent.next.left
                Parent = Parent.next
            LeftMost = LeftMost.left 
            Parent = LeftMost
        return root


