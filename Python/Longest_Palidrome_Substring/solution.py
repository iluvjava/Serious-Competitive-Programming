from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s # assert length of the string is at least 2. 
        if s == s[::-1]: return s
        DP = {}
        # II, JJ, both ends inclusive
        for II in range(len(s)):
            DP[II, II] = True
            DP[II, II - 1] = True
        BestIdx = (0, 0)
        BestLength = 0
        for LL in range(1, len(s)):
            for II in range(len(s) - LL):
                JJ = II + LL
                if s[II] == s[JJ]:
                    DP[II, JJ] = DP[II + 1, JJ - 1]
                else:
                    DP[II, JJ] = False
                if DP[II, JJ] and BestLength < JJ - II + 1:
                    BestIdx = (II, JJ)
                    BesetLength = JJ - II + 1
     
        return s[BestIdx[0]: BestIdx[1] + 1]
        