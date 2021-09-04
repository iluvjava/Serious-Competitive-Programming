from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        AnagramsMap = {}
        for Word in strs:
            Ana = "".join(sorted(Word))
            if Ana in AnagramsMap:
                AnagramsMap[Ana].append(Word)
            else:
                AnagramsMap[Ana] = [Word]
        return [L for L in AnagramsMap.values()]