from typing import *

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        MinLeft = [float("inf")]
        MaxRight = [float("-inf")]
        
        for II in range(len(nums)): 
            JJ = len(nums) - 1 - II
            N = nums[II]
            M = nums[JJ]
            MinLeft.append(min(MinLeft[-1], N))
            MaxRight.append(max(MaxRight[-1], M))
        MinLeft.pop(0)
        MaxRight.pop(-1)
        MaxRight = MaxRight[::-1]
        
        for II, E in enumerate(nums):
            if MinLeft[II] < E and E < MaxRight[II]: 
                return True
        return False