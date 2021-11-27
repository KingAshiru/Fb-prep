class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
        
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0])
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1])
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0
        
        return obstacleGrid[m - 1][n - 1]

    class Solution(object):
    def countPath(self, M, N, obstacleGrid, memo):
		if (M, N) in memo:
			return memo[(M, N)]
		
		if M == 0 and N == 0: # Reached destination
			return 1
		
		# If cell is invalid or cell has an obstacle, then no path.
		if M < 0 or N < 0 or obstacleGrid[M][N] == 1:
			return 0

		go_up = self.countPath(M-1, N, obstacleGrid, memo)
		go_left = self.countPath(M, N-1, obstacleGrid, memo)
		
		memo[(M, N)] = go_up + go_left
		
		return memo[(M, N)]
		
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M = len(obstacleGrid) - 1
        N = len(obstacleGrid[M]) - 1

        # Don't waste time if we can't find a path. 
        # i.e start and end destination must be free of obstacle.
        if obstacleGrid[0][0] == 1 or obstacleGrid[M][N] == 1:
            return 0

        memo = {}

        # Starting from the bottom-right corner and traversing to the top-left
        return self.countPath(M, N, obstacleGrid, memo)
