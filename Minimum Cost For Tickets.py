class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        ans = self.dfs(days, costs, 0, memo)
        return ans
    
    def dfs(self, days, costs, start, memo):
        ans = float("inf")
        n = len(days)
        if start >= n:
            return 0
        if start in memo:
            return memo[start]
        spans = [1, 7, 30]
        for i, c in enumerate(costs):
            curt = c
            span = spans[i]
            j = start
            while j < n:
                if days[j] - days[start] >= span:
                    break
                j += 1
            
            ans = min(ans, curt + self.dfs(days, costs, j, memo))
        
        memo[start] = ans
        return ans
