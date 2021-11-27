class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}
        word_dict = set(wordDict)
        
        def dfs(i):
            if i == len(s):
                return [""]
            if i in cache:
                return cache[i]
            res = []
            for j in range(i, len(s)):
                head = s[i:j+1]
                if head in word_dict:
                    temp = dfs(j+1)
                    for string in temp:
                        string = head + " " + string
                        res.append(string.strip())
            cache[i] = res
            return res
        
        return dfs(0)
        
