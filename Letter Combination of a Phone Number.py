class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_num = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        def dfs(res, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            next_num = digits[len(path)]
            for char in phone_num[next_num]:
                path.append(char)
                dfs(res, path)
                path.pop()
            
        res = []
        dfs(res, [])
        return res
