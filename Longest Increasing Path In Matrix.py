class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        # Initialize
        rows, cols = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        visited = [[0] * cols for _ in range(rows)]
        res = 0

        def dfs(i, j):
            # Check if visited
            if visited[i][j]:
                return visited[i][j]

            res = 1

            # work with neighbors
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]

                # for each direction we try to find a new count
                direction_count = 0
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if matrix[i][j] < matrix[next_i][next_j]:
                        direction_count = 1 + dfs(next_i, next_j)

                res = max(direction_count, res)

            visited[i][j] = res
            return res

        for row in range(rows):
            for col in range(cols):
                res = max(dfs(row, col), res)

        return res
