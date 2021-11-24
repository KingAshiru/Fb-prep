class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        
        def backtrack(paren, left, right):
            if len(paren) == n*2:
                res.append("".join(paren))
                return
            
            if left < n:
                paren.append('(')
                backtrack(paren, left + 1, right)
                paren.pop()
            
            if right < left:
                paren.append(')')
                backtrack(paren, left, right + 1)
                paren.pop()
            
        backtrack([], 0, 0)
        return res
