from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        Parents = [root]
        Children = []
        Level = 1
        Results = [[root.val]]
        while True: 
            for P in Parents: 
                if P.left is not None: 
                    Children.append(P.left)
                if P.right is not None: 
                    Children.append(P.right)
            # print(f"At Level: {Level}, Children Made: {[N.val for N in Children]}")
            if len(Children) == 0: 
                break
            Parents = Children 
            if Level %2 == 0: 
                Results.append(list(map(lambda x: x.val, Children)))
            else: 
                Results.append(list(map(lambda x: x.val, Children[::-1])))
            Children = []
            Level += 1
        
        return Results

