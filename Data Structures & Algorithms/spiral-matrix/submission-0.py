class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        final = []
        up = left = 0
        grid = matrix
        down = len(grid) - 1
        right = len(grid[0]) - 1

        while left <= right and up <= down:
            for i in range(left, right + 1):
                final.append(grid[up][i])
            up += 1

            for i in range(up, down + 1):
                final.append(grid[i][right])
            right -= 1

            if up <= down:
                for i in range(right, left - 1, -1):
                    final.append(grid[down][i])
                down -= 1
            
            if left <= right:
                for i in range(down, up - 1, -1):
                    final.append(grid[i][left])
                left += 1

        return final