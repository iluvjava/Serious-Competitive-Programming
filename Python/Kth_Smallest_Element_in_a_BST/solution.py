from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        NodeStates = {}
        Stack = [root]
        Queue = []
        while len(Stack) != 0:
            Node = Stack[-1]
            if Node is None: 
                Stack.pop()
                continue
            if Node not in NodeStates: 
                Stack.append(Node.left)
                NodeStates[Node] = 1
            else:
                if NodeStates[Node] == 1:
                    NodeStates[Node] = 2
                    Queue.append(Node.val)
                    Stack.append(Node.right)
                    pass
                else:
                    Stack.pop()
            if len(Queue) > k: 
                break
        return Queue[k-1]