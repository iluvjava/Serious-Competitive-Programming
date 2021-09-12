from typing import * 
class Solution:
    DigitsToLetters = {
            "2": "abc",
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: 
            return []
        Results = []
        def Recur(idx, stringBuild=""): 
            if idx >= len(digits): 
                Results.append(stringBuild)
                return
            for L in Solution.DigitsToLetters[digits[idx]]: 
                Recur(idx + 1, stringBuild + L)
        Recur(0)
        return Results