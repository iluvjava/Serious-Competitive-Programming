from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        S = set(nums)
        M = dict(zip(nums, range(len(nums))))
        AlreadyThere = set()
        Results = []
        for II in range(len(nums)): 
            for JJ in range(II + 1, len(nums)): 
                t = -(nums[II] + nums[JJ]) 
                Triplet = [nums[II], nums[JJ], t]
                Triplet.sort()
                HashTriplet = tuple(Triplet)
                if (t in S) and (M[t] > JJ) and (tuple(HashTriplet) not in AlreadyThere):
                    Results.append(Triplet)
                    AlreadyThere.add(HashTriplet)
        return Results

