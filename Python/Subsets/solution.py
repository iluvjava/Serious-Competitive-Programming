from typing import *


class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Subsets = []
        def Generate(idxStart = 0, indices=set()): 
            if idxStart == len(nums): 
                Subsets.append([nums[II] for II in indices])
                return
            indices.add(idxStart)
            Generate(idxStart + 1, indices)
            indices.remove(idxStart)
            Generate(idxStart + 1, indices)
        Generate()
        return Subsets
            