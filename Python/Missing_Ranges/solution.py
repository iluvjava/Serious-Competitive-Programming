class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def Convert(a, b):
            if a + 1 == b - 1: 
                return str(a + 1)
            else:
                return f"{str(a + 1)}->{str(b - 1)}"
        if len(nums) == 0: return [Convert(lower - 1, upper + 1)]
        Ranges = []
        if nums[0] > lower: Ranges.append(Convert(lower - 1, nums[0]))
        for II in range(len(nums) - 1): 
            JJ = II + 1
            L, R = nums[II], nums[JJ]
            if R - L == 1: continue
            Ranges.append(Convert(L, R))
        if nums[-1] < upper: Ranges.append(Convert(nums[-1], upper + 1))
        return Ranges
            