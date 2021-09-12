from typing import * 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def Swap(ii, jj):
            nums[ii], nums[jj] = nums[jj], nums[ii]
        def GeneratePermutation(idxStart=0):
            if idxStart == len(nums):
                yield nums[:]
            for II in range(idxStart, len(nums)): 
                Swap(idxStart, II)
                for Sub in GeneratePermutation(idxStart + 1): 
                    yield Sub
                Swap(idxStart, II)
        return list(GeneratePermutation())