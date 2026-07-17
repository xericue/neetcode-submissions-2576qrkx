class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, left = 0, 0
        right = len(matrix[0]) - 1
        down = len(matrix) - 1

        final = []

        while left <= right and up <= down:
            # do the easy not backwards ones first
            
            # up
            for i in range(left, right + 1):
                final.append(matrix[up][i])
            up += 1
            
            # right
            for i in range(up, down + 1):
                final.append(matrix[i][right])
            right -= 1

            # backwards ones
            # down - we couldve passed our condition so check
            if up <= down:
                for i in range(right, left - 1, -1):
                    final.append(matrix[down][i])
                down -= 1
            
            if left <= right:
                for i in range(down, up - 1, -1):
                    final.append(matrix[i][left])
                left += 1

        return final