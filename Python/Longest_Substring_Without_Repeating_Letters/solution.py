from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Result = 0
        if len(s) == 0: return 0
        II = 0
        JJ = 0
        S = set()
        while JJ != len(s):
            S.add(s[JJ])
            if len(S) != JJ - II + 1:
                while s[II] != s[JJ]:
                    S.remove(s[II])
                    II += 1
                II += 1
            else:
                Result = max(JJ - II + 1, Result)
            JJ += 1
        return Result