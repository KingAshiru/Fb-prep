class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = 1
                    break
        
        return dp[-1] == 1
