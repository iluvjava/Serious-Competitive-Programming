from typing import * 


class Solution:
    # 
    # Number: needs this many ) to balance previous expression at the right hand side
    def generateParenthesis(self, n: int) -> List[str]:
        ValidExpression = []
        def Recur(expression, optionsLeft:int, toBalance:int=0):
            if (optionsLeft - toBalance)%2 == 1: 
                return 
            if optionsLeft < toBalance: 
                return 
            if optionsLeft == 0 and toBalance == 0: 
                ValidExpression.append("".join(expression))
                return
            expression.append("(")
            Recur(expression, optionsLeft - 1, toBalance + 1)
            expression.pop(-1)
            if toBalance >= 1: 
                expression.append(")")
                Recur(expression, optionsLeft - 1, toBalance - 1)
                expression.pop(-1)
        Recur([], 2*n)
        return ValidExpression
        